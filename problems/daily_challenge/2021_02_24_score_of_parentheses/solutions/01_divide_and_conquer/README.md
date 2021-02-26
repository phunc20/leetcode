Approach 1: Divide and Conquer
Intuition

Split the string into S = A + B where A and B are balanced parentheses strings, and A is the smallest possible non-empty prefix of S.

Algorithm

Call a balanced string primitive if it cannot be partitioned into two non-empty balanced strings.

By keeping track of balance (the number of ( parentheses minus the number of ) parentheses), we can partition S into primitive substrings S = P_1 + P_2 + ... + P_n. Then, score(S) = score(P_1) + score(P_2) + ... + score(P_n), by definition.

For each primitive substring (S[i], S[i+1], ..., S[k]), if the string is length 2, then the score of this string is 1. Otherwise, it's twice the score of the substring (S[i+1], S[i+2], ..., S[k-1]).


### Complexity Analysis

Time Complexity: O(N^2)O(N 
2
 ), where NN is the length of S. An example worst case is (((((((....))))))).

Space Complexity: O(N)O(N), the size of the implied call stack.
