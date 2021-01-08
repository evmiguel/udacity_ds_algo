from queue import PriorityQueue
import sys

class HuffmanTree:
    def __init__(self, value=None, frequency=None, left=None, right=None, bit=None):
        self.value = value
        self.frequency = frequency
        self.left = left
        self.right = right
        self.bit = bit
    def __lt__(self, obj):
        return self.frequency < obj.frequency
    def __le__(self, obj):
        return self.frequency <= obj.frequency

def merge(node1, node2):
    if isinstance(node1.value, str) and isinstance(node2.value, str):
        return HuffmanTree(value=HuffmanTree(), frequency=node1.frequency+node2.frequency, left=node1, right=node2)
    elif isinstance(node1.value, HuffmanTree) and isinstance(node2, str):
        return HuffmanTree(value=HuffmanTree(), frequency=node1.frequency+node2.frequency, left=node1, right=node2)
    elif isinstance(node1, HuffmanTree) and isinstance(node2, HuffmanTree):
        return HuffmanTree(value=HuffmanTree(), frequency=node1.frequency+node2.frequency, left=node1, right=node2)


def generate_char_frequencies(data):
    frequencies = {}
    for char in data:
        if frequencies.get(char) is None:
            frequencies[char] = 1
        else:
            frequencies[char] += 1
    return frequencies

def char_frequencies_to_priority_queue(char_frequencies):
    pq = PriorityQueue()
    for item in char_frequencies.items():
        node = HuffmanTree(item[0], item[1])
        pq.put((item[1], node))
    return pq

'''
This function is assuming that the
priority queue has more than two nodes.
'''
def create_huffman_tree(pq):
    if pq.qsize() == 1:
        node = pq.get(block=False)[1]
        return HuffmanTree(value=HuffmanTree(), frequency=node.frequency, left=node, right=None)
    while pq.qsize() > 1:
        min_elem_1 = pq.get(block=False)
        min_elem_2 = pq.get(block=False)
        tree = merge(min_elem_1[1], min_elem_2[1])
        pq.put((tree.frequency, tree))
    tree = pq.get(block=False)[1]
    return tree

def set_huffman_tree_bits(tree, encoding_map, huffman_code):
    if isinstance(tree.value, str):
        encoding_map[tree.value] = huffman_code
        return encoding_map
    else:
        if tree.left:
            tree.left.bit = 0
            set_huffman_tree_bits(tree.left, encoding_map, huffman_code+str(tree.left.bit))

        if tree.right:
            tree.right.bit = 1
            set_huffman_tree_bits(tree.right, encoding_map, huffman_code+str(tree.right.bit))
    return encoding_map

def encode(encoding_map, data):
    encoding = ''
    for char in data:
        encoding += encoding_map[char]
    return encoding


def huffman_encoding(data):
    assert data
    char_frequencies = generate_char_frequencies(data)
    char_pq = char_frequencies_to_priority_queue(char_frequencies)
    tree = create_huffman_tree(char_pq)
    encoding_map = set_huffman_tree_bits(tree, {}, '')
    encoded_data = encode(encoding_map, data)
    return encoded_data, tree

def huffman_decoding(data,tree):
    decoded_data = ''
    node = tree
    bit_position = 0
    while bit_position < len(data):
        while not isinstance(node.value, str):
            if data[bit_position] == '0':
                node = node.left
            else:
                node = node.right
            bit_position += 1
        decoded_data += node.value
        node = tree
    return decoded_data

if __name__ == "__main__":
    codes = {}

    # First Test - valid string
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # 69
    print ("The content of the data is: {}\n".format(a_great_sentence)) # The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # 36
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # 1000111111100100001101110000101110110110100011111111001101010011100001

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 69
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # The bird is the word

    # Second Test - empty string
    empty_string = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(empty_string))) # 49
    print ("The content of the data is: {}\n".format(empty_string)) # Empty string
    try:
        encoded_data, tree = huffman_encoding(empty_string) # Assertion error
    except AssertionError:
        pass

    # Third Test - single character
    char = "a"
    print ("The size of the data is: {}\n".format(sys.getsizeof(char))) # 50
    print ("The content of the data is: {}\n".format(char)) # Empty string
    encoded_data, tree = huffman_encoding(char)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # 24
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # 0

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 50
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # a

    # Fourth Test - same character repeated
    repeated = "AAAAAAAAAA"
    print ("The size of the data is: {}\n".format(sys.getsizeof(repeated))) # 59
    print ("The content of the data is: {}\n".format(repeated)) # AAAAAAAAAA
    encoded_data, tree = huffman_encoding(repeated)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # 24
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # 0000000000

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 59
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # AAAAAAAAAA
