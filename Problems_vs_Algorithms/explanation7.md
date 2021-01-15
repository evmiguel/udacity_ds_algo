# Explanation

## RouteNode
I decided to use a dictionary for the `children`
field  for O(1) lookup and O(1) insertion, with
the dictionary taking about O(n) space, n being
the number of nodes in the trie. 

## RouteTrie
Given that the `insert` function in RouteNode is
O(1) time, the `insert` function in RouteTrie iterates
over the the split path, taking O(n) time and O(1)
space, since the split path is being passed. The`find` 
also takes O(n) time for the number of strings in split 
path and taking O(1) space because the split path array
is being passed.


## Router
The router is the main API. Given this, I decided to
handler the trailing slashes, root handler, and not found 
handler in the router. I also decided that the path
and handler assertions should be in this class so that
the `RouteTrie` and `RouteNode` classes do not have
to deal with input validation. The `add_handler` class
takes O(n) time because it is dependent on the `insert`
function of the `RouteTrie` class, and it takes O(n)
space because it depends on the `split_path` function,
which returns an array of size n. The `lookup` function
also takes O(n) time because it is dependent on the `find`
function of `RouteTrie` and takes O(n) space because it
uses the `split_path` function.