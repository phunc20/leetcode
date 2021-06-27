class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
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
            L = extract_layer(topleft, h, w)
            if kmod != 0:
                L = L[kmod:] + L[:kmod]
            reassign(topleft, h, w, L)
            h -= 2
            w -= 2
            topleft += 1
        return grid




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

