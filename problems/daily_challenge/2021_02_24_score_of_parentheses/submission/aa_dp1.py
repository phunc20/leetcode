class Solution:
    memo = {}
    def scoreOfParentheses(self, S: str) -> int:
        if S in Solution.memo:
            return Solution.memo[S]
        if S == "()":
            score = 1
            Solution.memo[S] = score 
            return score
        else:
            statistics = {"(": 1, ")": 0}  # The 0-th index substring must be "("
            def balanced(D):
                return D["("] == D[")"]
            i = 1
            ## The following loop will end for sure because S is a balanced parentheses string.
            while not balanced(statistics):
                statistics[S[i]] += 1
                i += 1
            ## Check whether or not we have touched len(S) - 1, i.e. the last index, and react accordingly.
            if i == len(S):
                score = 2*Solution.scoreOfParentheses(self, S[1:-1])
            else:
                score = Solution.scoreOfParentheses(self, S[:i]) + Solution.scoreOfParentheses(self, S[i:])
            Solution.memo[S] = score
            return score
