# Explanation

The rationale for this problem is to sort the
elements in descending order and then build
the two integers up by alternating the integer
being added. I got this from the forum:
(https://knowledge.udacity.com/questions/307603)

Given that we are not allowed a built in sorting
function, I implemented merge sort in descending
order, which takes O(n log n) time and O(n log n)
space, though it can theoretically be O(1) if I
had implemented it in place.

Then, building up the integers takes O(n) time
and O(1) space. So, the function, `rearrange_digits`,
takes O(n log n) time and O(n log n) space overall.