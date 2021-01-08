class Node():
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        assert capacity > 0
        self.capacity = capacity
        self.num_items = 0
        self.head = None
        self.tail = None
        self.map = {}

    def append(self, key, value):
        node = Node(key, value)
        if self.head is None:
            self.map[key] = node
            self.head = node
            self.tail = self.head
        else:
            self.map[key] = node
            self.tail.next = node
            self.tail.next.prev = self.tail
            self.tail = node

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        node = self.map.get(key)
        if node is None:
            return -1
        
        if self.capacity > 1:
            if node == self.head:
                self.head = node.next
                self.head.prev = None
            elif node is not self.tail:
                node.prev.next = node.next
                node.next.prev = node.prev

            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.num_items == self.capacity:
            if self.capacity == 1:
                self.map.pop(self.head.key)
                self.head = None
            else:
                node = self.head
                self.head = node.next
                self.head.prev = None
                self.map.pop(node.key)
                node = None
            self.num_items -= 1
        self.append(key, value)
        self.num_items += 1

    # Utility function
    def print_values(self):
        node = self.head
        string = ''
        while node:
            string += '{} '.format(node.value)
            node = node.next
        print(string)


cache = LRU_Cache(5)

cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(4, 4)
cache.print_values()
# 1 2 3 4

cache.get(1)
cache.get(2)
cache.print_values()
# 3 4 1 2

cache.set(5, 5)
cache.set(6, 6)
cache.print_values()
# 4 2 1 5 6

#------------------

our_cache=LRU_Cache(1)
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
our_cache.set(4,4)
print(our_cache.get(4)) # 4
print(our_cache.get(1)) # -1

our_cache.set(2,4)
print(our_cache.get(2)) # 4

# Edge case - Set and Get None
our_cache.set(None,1)
print(our_cache.get(None)) # 1
print(our_cache.get(2)) # -1

# Edge case - Set and Get Negative
our_cache.set(-1,100)
print(our_cache.get(-1)) # 100
print(our_cache.get(None)) # -1

#-------------------------
# This implementation does not support cache's of size 0
try:
    our_cache=LRU_Cache(0)
    our_cache.set(1,1)
except AssertionError:
    pass

