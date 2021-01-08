# Explanation
Given that we could not use the `os.walk()` function,
I decided to return the output of a recursive function
since the file structure resembles a tree. To find the
files, the function is essentially doing a depth first
search. The Big O time complexity of DFS is O(V+E) and also
taking O(V+E) space.

For this implementation, I've decided that None type
and empty string suffixes return an empty array. I've
also decided to add an assertion to validate the input
path.