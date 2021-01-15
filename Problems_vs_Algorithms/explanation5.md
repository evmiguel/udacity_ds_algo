# Explanation

## TrieNode
I decided to use a dictionary for the `children`
field for O(1) lookup and O(1) insertion, with
the dictionary taking about O(n) space, n being
the number of nodes in the trie. The`suffixes` 
function runs in O(V+E) time because
it is essentially a depth first search to each
leaf; it also takes of O(V+E) space because of
the number of calls on the stack.

## Trie
Given that the `insert` function in TrieNode is
O(1) time, the `insert` function in Trie iterates
over the the word, taking O(n) time, and the space
is described above in the TrieNode section. The
`find` also takes O(n) time for the number of characters
in the prefix and taking O(1) space.