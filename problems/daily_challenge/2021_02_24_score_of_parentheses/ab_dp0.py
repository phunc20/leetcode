#class Solution:
#    def scoreOfParentheses(self, S: str) -> int:

memo = {}
def scoreOfParentheses(S):
    if S in memo:
        return memo[S]
    if S == "()":
        score = 1
        memo[S] = score 
        return score
    else:
        statistics = {"(": 0, ")": 0}
        def balanced(D):
            if D["("] == 0 and D[")"] == 0:
                return False
            else:
                return D["("] == D[")"]
        i = 0
        ## The following loop will end for sure because S is a balanced parentheses string.
        while not balanced(statistics):
            statistics[S[i]] += 1
            i += 1
        ## Check whether or not we have touched len(S) - 1, i.e. the last index, and react accordingly.
        #print(f"i = {i}, len(S) = {len(S)}")
        if i == len(S):
            score = 2*scoreOfParentheses(S[1:-1])
        else:
            score = scoreOfParentheses(S[:i]) + scoreOfParentheses(S[i:])
        memo[S] = score
        return score


def example(id_, input_, expected):
    print(f"Example {id_}")
    output = scoreOfParentheses(input_)
    if  output == expected:
        print("Correct")
    else:
        print(f"Incorrect. input = \"{input_}\", output = {output}, expected = {expected}")


if __name__ == "__main__":
    example(id_=1, input_="()", expected=1)
    example(id_=2, input_="(())", expected=2)
    example(id_=3, input_="()()", expected=2)
    example(id_=4, input_="(()(()))", expected=6)
