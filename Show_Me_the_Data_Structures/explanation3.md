# Explanation
I decided to use the Python `queue` library's PriorityQueue
to help ease implementation. I also decided to break up
the encoding into different helper functions.

I decided to put an assertion of the data in `huffman_encoding`
to ensure that there is data to encode.

The `generate_char_frequencies` function runs in O(n) time 
and O(n) space. The `char_frequencies_to_priority_queue` also
runs in O(n) time and O(n) space. The `merge` function runs in
O(1) time and O(1) space because it only checks the node type
and creates a new tree based off of that. The `set_huffman_tree_bits`
is essentially a depth first search, so the runtime is O(V+E)
and the space is O(1) because the function is utilizing an existing tree.
The `encode` function runs in O(n) time with O(n) space.
The `huffman_decoding` function is O(nd), where d is the depth of the
tree and n is the length of the string.