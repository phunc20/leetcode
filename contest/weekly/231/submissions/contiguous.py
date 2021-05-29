class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if "0" not in s:
            return True
        index_first0 = 1
        not_0 = s[index_first0] != "0"
        #while not_0 or index_first0 >= len(s):
        #    index_first0 += 1
        #    not_0 = s[index_first0] != "0"
        #if not not_0:
        while not_0:
            index_first0 += 1
            not_0 = s[index_first0] != "0"
        tail = set(s[index_first0:])
        return len(tail) == 1

def test_case(k, s, expected):
    print(f"Test case {k:02d}")
    ans = checkOnesSegment(s)
    if ans == expected:
        print("Correct.")
    else:
        print(f"Incorrect. ans = {ans}, expected = {expected}")


if __name__ == "__main__":
    test_case(1, "1001", False)
    test_case(2, "110", True)

