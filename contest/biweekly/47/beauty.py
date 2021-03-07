#class Solution:
#    def beautySum(self, s: str) -> int:
        
def beautySum(s):
    if len(s) <= 2:
        return 0
    # Now assured that len(s) >= 3.
    somme = 0
    for head in range(len(s) - 2):
        statistics = {s[head]: 1}
        if s[head+1] in statistics:
            statistics[s[head+1]] += 1
        else:
            statistics[s[head+1]] = 1
        for tail in range(head+2, len(s)):
            if s[tail] in statistics:
                statistics[s[tail]] += 1
            else:
                statistics[s[tail]] = 1
            somme += max(statistics.values()) - min(statistics.values())
    return somme

def test_case(k, s, expected):
    print(f"Test case {k:02d}")
    ans = beautySum(s)
    if ans == expected:
        print("Correct.")
    else:
        print(f"Incorrect. ans = {ans}, expected = {expected}")


if __name__ == "__main__":
    test_case(1, "aabcb", 5)
    test_case(2, "aabcbaa", 17)
