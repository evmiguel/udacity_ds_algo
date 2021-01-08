# Explanation

This function utilizes binary search and the
rule that, for a given number n,

1 <= sqrt(n) <= n

In other words, the square root of the number
is between 1 and the number. Therefore, we can
compare a number m^2 to n, where m is the midpoint
between 1 and n. Just as with binary search,
if m^2 > n, we can move the rightmost number to
the left, and if m^2 < n, we can move the leftmost
number to the right.

This function runs in O(log n) time, and it takes
O(1) space.