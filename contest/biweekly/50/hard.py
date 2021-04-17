#class Solution:
#    def makeStringSorted(self, s: str) -> int:


def makeStringSorted(s):
    modulo = 10**9 + 7
    pass



def test(points, queries, expected):
    sol = countPoints(points, queries)
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
    points = [[1,3],[3,3],[5,3],[2,2]]
    queries = [[2,3,1],[4,3,1],[1,1,2]]
    expected = [3,2,2]
    test(points, queries, expected)

