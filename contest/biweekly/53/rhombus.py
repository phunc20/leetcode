#class Solution:
#    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
def getBiggestThree(grid):
    pass


def test(grid, expected):
    sol = getBiggestThree(grid)
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
    grid
    expected = 1
    test(grid, expected)

    test_id += 1
    print(f"testcase {test_id}")
    grid
    expected = 4
    test(grid, expected)
    


