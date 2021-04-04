#class Solution:
#    def truncateSentence(self, s: str, k: int) -> str:
#        pass
"""
Idea 1: split()

Idea 2: find the number of spaces/blanks
"""

def truncateSentence(s, k):
    words = s.split()
    return " ".join(words[:k])

def test(s, k, expected):
    ans = truncateSentence(s, k)
    if ans == expected:
        print("Congratulations!")
    else:
        print("Almost there.")
        print(f"ans = {ans}")
        print(f"expected = {expected}")


if __name__ == "__main__":
    s = "Hello how are you Contestant"
    k = 4
    expected = "Hello how are you"
    test(s,k,expected)

    s = "What is the solution to this problem"
    k = 4
    expected = "What is the solution"
    test(s,k,expected)

    s = "chopper is not a tanuki"
    k = 5
    expected = "chopper is not a tanuki"
    test(s,k,expected)
