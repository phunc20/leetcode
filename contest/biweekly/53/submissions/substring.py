class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-2):
            substring = s[i:i+3]
            if len(set(substring)) == 3:
                count += 1
        return count



def test(s, expected):
    sol = countGoodSubstrings(s)
    if sol == expected:
        print("Congratulations!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
    print()

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    print(f"testcase {test_id}")
    s = "xyzzaz"
    expected = 1
    test(s, expected)

    test_id += 1
    print(f"testcase {test_id}")
    s = "aababcabc"
    expected = 4
    test(s, expected)
    


