### The bug/problem of `memo_recursion.c` (on TestCase11)
is probably that `memo` is of type `float` and when we return the entries of `memo` to the function
`int maximumScore(int* nums, int numsSize, int* multipliers, int multipliersSize)`, the conversion btw
`float` and `int` causes problems.

In `debug_memo_recursion.c`, I created an array separately to track whether or not that `(left, right)` entry
has been filled. And this makes `debug_memo_recursion.c` pass TestCase 11.

Note that both `debug_memo_recursion.c` and `../py/memo_recursion.py` passed only `28/59` of the testcases.
