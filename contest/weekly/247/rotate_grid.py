#class Solution:
#    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
               
def rotateGrid(grid, k):
    """
    Let's rotate the grid layer after layer.
    """
    def extract_layer(topleft, h, w):
        ## Implementation01
        #L = [grid[topleft][topleft + j] for j in range(w)]
        #L += [grid[topleft + i][topleft + (w-1)] for j in range(1, h)]
        #L += [grid[topleft + (h-1)][topleft + j] for j in reversed(range(w-1))]
        #L += [grid[topleft + i][topleft] for i in reversed(range(1, h-1))]

        # Implementation02
        L = [grid[topleft][topleft + j] for j in range(w)]
        L += [grid[topleft + i][topleft + (w-1)] for i in range(h)][1:]
        L += [grid[topleft + (h-1)][topleft + j] for j in reversed(range(w))][1:]
        L += [grid[topleft + (h-1)][topleft + j] for j in reversed(range(w))][1:]
        L += [grid[topleft + i][topleft] for i in reversed(range(h))][1:-1]
        return L
    def reassign(topleft, h, w, L):
        ## top side
        for j in range(w):
            #grid[topleft][topleft + j] = L[j - topleft]
            grid[topleft][topleft + j] = L[j]
        ## right side
        for i in range(h):
            grid[topleft + i][topleft + (w-1)] = L[w-1+i]
        ## bottom side
        for j in reversed(range(w)):
            grid[topleft + (h-1)][topleft + j] = L[-(h-1)-j]
        ## left side
        for i in reversed(range(h)):
            grid[topleft + i][topleft] = L[-i]
    m = len(grid)
    n = len(grid[0])
    h = m
    w = n
    topleft = 0
    while h > 0 and w > 0:
        kmod = k % ((h+w)*2 - 4)
        if kmod != 0:
            L = extract_layer(topleft, h, w)
            L = L[kmod:] + L[:kmod]
            reassign(topleft, h, w, L)
        h -= 2
        w -= 2
        topleft += 1
    return grid

def visualize(grid):
    pass


counter = 1
def test(grid, k, expected):
    global counter
    print(f"(Test {counter:02d})")
    sol = rotateGrid(grid, k)
    if sol == expected :
        print("Congrats!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
    print()
    counter += 1



if __name__ == "__main__":
    grid = [[40,10],[30,20]]
    k = 1
    expected = [[10,20],[40,30]]
    test(grid, k, expected)

    grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    k = 2
    expected = [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
    test(grid, k, expected)

    grid = [[3970,1906,3608,298,3072,3546,1502,773,4388,3115,747,3937],[2822,304,4179,1780,1709,1058,3645,681,2910,2513,4357,1038],[4471,2443,218,550,2766,4780,1997,1672,4095,161,4645,3838],[2035,2350,3653,4127,3208,4717,4347,3452,1601,3725,3060,2270],[188,2278,81,3454,3204,1897,2862,4381,3704,2587,743,3832],[996,4499,66,2742,1761,1189,608,509,2344,3271,3076,108],[3274,2042,2157,3226,2938,3766,2610,4510,219,1276,3712,4143],[744,234,2159,4478,4161,4549,4214,4272,701,4376,3110,4896],[4431,1011,757,2690,83,3546,946,1122,2216,3944,2715,2842],[898,4087,703,4153,3297,2968,3268,4717,1922,2527,3139,1516],[1086,1090,302,1273,2292,234,3268,2284,4203,3838,2227,3651],[2055,4406,2278,3351,3217,2506,4525,233,3829,63,4470,3170],[3797,3276,1755,1727,1131,4108,3633,1835,1345,1293,2778,2805],[1215,84,282,2721,2360,2321,1435,2617,1202,2876,3420,3034]]
    k = 405548684
    expected = [[188,2035,4471,2822,3970,1906,3608,298,3072,3546,1502,773],[996,1058,3645,681,2910,2513,4357,4645,3060,743,3076,4388],[3274,1709,4376,3944,2527,3838,63,3829,233,4525,3712,3115],[744,1780,1276,4478,3226,2742,3454,4127,3208,2506,3110,747],[4431,4179,3271,2690,83,4161,2938,1761,4717,3217,2715,3937],[898,304,2587,4153,3297,946,3546,3204,4347,3351,3139,1038],[1086,2443,3725,1273,2968,4214,4549,1897,3452,2278,2227,3838],[2055,2350,161,2292,3268,2610,3766,2862,1601,302,4470,2270],[3797,2278,4095,234,4717,608,1189,4381,3704,703,2778,3832],[1215,4499,1672,3268,1122,4272,4510,509,2344,757,1293,108],[84,2042,1997,2284,4203,1922,2216,701,219,2159,1345,4143],[282,234,4780,2766,550,218,3653,81,66,2157,1835,4896],[2721,1011,4087,1090,4406,3276,1755,1727,1131,4108,3633,2842],[2360,2321,1435,2617,1202,2876,3420,3034,2805,3170,3651,1516]]
    test(grid, k, expected)
