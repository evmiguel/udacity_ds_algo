# Explanation
Given that the Blockchain is implemented as a Linked List,
the `add_node` method runs in O(1) time and takes O(n) space,
where n is the number of nodes. The `print` function
runs in O(n) time and O(n) space due to the number of calls
on the stack.

I decided to support None type and bool type with the line
`str_to_encode = str(self.data)+self.previous_hash if self.previous_hash else str(self.data)`.

This implementation also supports nodes with the same timestamp. The chain
also ends if all the data is stripped from a block.