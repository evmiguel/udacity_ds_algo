# Explanation

I decided to use recursion to be able
to traverse the groups of groups. If the
group chains were larger, this function could
grow very unwieldy. The Big O notation for this
function can be O(n^p) where n is the number of groups
and p is the number of total groups being visited.
Worst case scenario, the space complexity will
also be O(n^p) because of the number of functions
calls on the stack.

This implementation asserts that the group is
a valid object.
