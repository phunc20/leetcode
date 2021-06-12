class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        S = set(range(left, right+1))
        for start, end in ranges:
            if end < left or start > right:
                continue
            else:
                S -= set(range(start, end+1))
        return len(S) == 0


def test(ranges, left, right, expected):
    sol = isCovered(ranges, left, right)
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
    ranges = [[1,2],[3,4],[5,6]]
    left = 2
    right = 5
    expected = True
    test(ranges, left, right, expected)

    test_id += 1
    print(f"testcase {test_id}")
    ranges = [[1,10],[10,20]]
    left = 21
    right = 21
    expected = False
    test(ranges, left, right, expected)
    


