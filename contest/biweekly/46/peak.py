#class Solution:
#    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        
def highestPeak(isWater):
    m = len(isWater)
    n = len(isWater[0])
    def oneize_surrounding(W, H, ii, jj):
        for incr_ii, incr_jj in ((0,1), (1,0), (0,-1), (-1,0)):
            iii = ii+incr_ii
            jjj = jj+incr_jj
            if (0 <= iii < m) and (0 <= jjj < n) and (not W[iii][jjj]):
                H[iii][jjj] = 1
    def fill_me(k, H, ii, jj):
        #print(f"H({ii}, {jj}) = {H[ii][jj]}")
        minimum = None
        for incr_ii, incr_jj in ((0,1), (1,0), (0,-1), (-1,0)):
            iii = ii+incr_ii
            jjj = jj+incr_jj
            #print(f"iii, jjj = {iii}, {jjj}")
            #if (0 <= iii < m) and (0 <= jjj < n):
            #    print(f"H({iii}, {jjj}) = {H[iii][jjj]}")
            if (0 <= iii < m) and (0 <= jjj < n) and (H[iii][jjj] is not None):
                #print(f"H({iii}, {jjj}) = {H[iii][jjj]}")
                if minimum is None:
                    minimum = H[iii][jjj]
                elif minimum > H[iii][jjj]:
                    minimum = H[iii][jjj]
        if minimum is not None:
            H[ii][jj] = minimum + 1
            return k - 1
        else:
            return k

    heights = [[None for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if isWater[i][j]:
                heights[i][j] = 0
                oneize_surrounding(isWater, heights, i, j)

    n_None_left = 0
    for i in range(m):
        for j in range(n):
            if heights[i][j] is None:
                n_None_left += 1
    #print(f"heights = {heights}")
    while n_None_left > 0:
        #print(f"heights = {heights}")
        #print(f"n_None_left = {n_None_left}")
        for i in range(m):
            for j in range(n):
                if heights[i][j] is not None:
                    continue
                else:
                    n_None_left = fill_me(n_None_left, heights, i, j)
    return heights


if __name__ == "__main__":
    isWater = [[0,1],[0,0]]
    print(f"isWater = {isWater}")
    print(f"ans = {highestPeak(isWater)}")
    isWater = [[0,0,1],[1,0,0],[0,0,0]]
    print(f"isWater = {isWater}")
    print(f"ans = {highestPeak(isWater)}")
    isWater = [[0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0]]
    expected = [[2,1,2,3,2,1,0,1],[1,0,1,2,3,2,1,2],[2,1,2,3,4,3,2,3],[3,2,3,4,5,4,3,4],[4,3,3,4,4,3,2,3],[4,3,2,3,3,2,1,2],[3,2,1,2,2,1,0,1],[2,1,0,1,2,2,1,2]]
    print(f"isWater = {isWater}")
    #print(f"ans = {highestPeak(isWater)}")
    print(f'{"Correct" if highestPeak(isWater) == expected else "Incorrect"}')

