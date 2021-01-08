# Explanation
The LRU cache uses two data structures, a dictionary and
a doubly linked list. The dictionary allows for O(1) access
to the node and the doubly linked list allows for O(1) insertion
and deletion. The space complexity is O(n), where n is the
number of nodes set.

The LRU cache supports setting None values, as Python also
supports having None as a dictionary key. This implementation
does not support caches of size 0.