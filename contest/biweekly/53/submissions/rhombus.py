class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        ## (?) can the inside functoin use the grid outside, i.e.
        ## w/o needing to put it again in its args?
        def rhombus_sums(grid, row, col):
            """
            Find all rhombus sums starting at `rowcol` downwards

            arg
                row, int
                    0 <= row <= m-1
                col, int
                    0 <= col <= n-1
            return
                S_sums, set of rhombus sums
            """
            m = len(grid)
            n = len(grid[0])
            #print(row, col)
            S_sums = set([grid[row][col]])
            side = 1
            while fit(m, n, row, col, side):
                sum_ = sum(grid[member[0]][member[1]] for member in members(row, col, side))
                S_sums.add(sum_)
                side += 1
            return S_sums

        def fit(m, n, row, col, side):
            ## h and v stands for horizontal and vertical
            h_fit = (col + side < n) and (col - side >= 0)
            if not h_fit:
                return False
            v_fit = row + 2*side < m
            if v_fit:
                return True
            else:
                return False

        def members(row, col, side):
            right_moves = list(range(1, side+1)) + list(range(side-1, -1, -1))
            left_moves = list(range(-1, -side-1, -1)) + list(range(-side+1, 1))
            down_moves = list(range(1, 2*side+1))
            S_members = set([(row, col)])
            for r_mv, d_mv in zip(right_moves, down_moves):
                new_member = (row + d_mv, col + r_mv)
                S_members.add(new_member)
            for l_mv, d_mv in zip(left_moves, down_moves):
                new_member = (row + d_mv, col + l_mv)
                S_members.add(new_member)
            return S_members

        m = len(grid)
        n = len(grid[0])
        S_rhombus_sums = set()
        ## For each position (i, j) we find all downward rhombus square starting
        ## from that position,
        for row in range(m):
            for col in range(n):
                S_rhombus_sums |= rhombus_sums(grid, row, col)
        if len(S_rhombus_sums) < 3:
            return sorted(S_rhombus_sums, reverse=True)
        else:
            return sorted(S_rhombus_sums, reverse=True)[:3]


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
    grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
    expected = [228,216,211]
    test(grid, expected)

    test_id += 1
    print(f"testcase {test_id}")
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    expected = [20,9,8]
    test(grid, expected)
    
    test_id += 1
    print(f"testcase {test_id}")
    grid = [[7,7,7]]
    expected = [7]
    test(grid, expected)


