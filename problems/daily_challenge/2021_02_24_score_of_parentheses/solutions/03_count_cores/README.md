# Approach 3: Count Cores
## Intuition
The final sum will be a sum of powers of 2, as every core (a substring (), with score 1) will have it's score multiplied by 2 for each exterior set of parentheses that contains that core.

## Algorithm
Keep track of the balance of the string, as defined in Approach #1. For every ) that immediately follows a (, the answer is 1 << balance, as balance is the number of exterior set of parentheses that contains this core.

## Complexity Analysis
- Time Complexity: O(N)O(N), where NN is the length of S.
- Space Complexity: O(1)O(1).
