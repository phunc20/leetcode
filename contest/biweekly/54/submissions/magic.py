class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_k = n if n < m else m
        
        def is_magic(top_left, bottom_right):
            res = True
            row_start = top_left[0]
            row_end = bottom_right[0]
            col_start = top_left[1]
            col_end = bottom_right[1]
            side_len = row_end - row_start + 1
            diag_sum = sum(grid[row_start + i][col_start + i] for i in range(side_len))
            # Examine the row sums
            for row in range(row_start, row_end + 1):
                row_sum = sum(grid[row][col_start + i] for i in range(side_len))
                if row_sum != diag_sum:
                    res = False
                    return res
            # Examine the col sums
            for col in range(col_start, col_end + 1):
                col_sum = sum(grid[row_start + i][col] for i in range(side_len))
                if col_sum != diag_sum:
                    res = False
                    return res
            # Examine the anti diagonal sum
            anti_sum = sum(grid[row_end - i][col_start + i] for i in range(side_len))
            if anti_sum != diag_sum:
                res = False
            return res

        for k in range(max_k, 1, -1):
            for row in range(m-k+1):
                for col in range(n-k+1):
                    top_left = (row, col)
                    bottom_right = (row+k-1, col+k-1)
                    if is_magic(top_left, bottom_right):
                        return k
        return 1
