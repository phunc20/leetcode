# Approach 2: Stack
## Intuition and Algorithm

Every position in the string has a depth - some number of matching parentheses surrounding it. For example, the dot in (()(.())) has depth 2, because of these parentheses: (__(.__))

Our goal is to maintain the score at the current depth we are on. When we see an opening bracket, we increase our depth, and our score at the new depth is 0. When we see a closing bracket, we add twice the score of the previous deeper part - except when counting (), which has a score of 1.

For example, when counting (()(())), our stack will look like this:

- [0, 0] after parsing (
- [0, 0, 0] after (
- [0, 1] after )
- [0, 1, 0] after (
- [0, 1, 0, 0] after (
- [0, 1, 1] after )
- [0, 3] after )
- [6] after )

## Complexity Analysis

- Time Complexity: O(N), where NN is the length of S.
- Space Complexity: O(N), the size of the stack.
