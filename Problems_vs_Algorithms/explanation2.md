# Explanation
There are two general solution to search for the number:
    - Linear search: O(n) time, O(1) space
    - Binary search: O(log n) time, O(1) space

What makes this problem interesting is that the input list
is rotated at a specific point. To solve this, the general 
solution is to:
    - Find the pivot point that the array is rotated upon
    - Run a binary search either on the left of the pivot point
        or on the right of the pivot point.

We know that binary search runs in O(log n) time. However, this
search would be no better than linear search if we cannot
guarantee that finding the pivot point is also faster than O(n).
Fortunately, we can modify binary search to find the pivot point
in O(log n) time. Therefore, the `rotated_array_search` function
runs in O(log n) time and O(1) space,

This function does not support target values that are not integers.