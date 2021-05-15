def rotateTheBox(box):
    OBSTACLE = "*"
    ROCK = "#"
    EMPTY = "."
    ## This is matrix transpose, not 90-degree clockwise rotation.
    #def rotate(array2D):
    #    m, n = len(array2D), len(array2D[0])
    #    res = [["x" for _ in range(m)] for _ in range(n)]
    #    for i in range(m):
    #        for j in range(n):
    #            res[j][i] = array2D[i][j]
    #    return res

    def rotate(array2D):
        m, n = len(array2D), len(array2D[0])
        res = [["x" for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][-(i+1)] = array2D[i][j]
        return res

    def find_next_obstacle(start, row):
        """
        start exclusive
        """
        n = len(row)
        for i in range(start+1, n):
            if row[i] == OBSTACLE:
                return i
        return n

    def find_next_non_obstacle(start, row):
        """
        start inclusive
        """
        n = len(row)
        for i in range(start, n):
            if row[i] == OBSTACLE:
                continue
            else:
                return i
        return n

    print(f"box (before) = {box}")
    for row in box:
        left = 0
        while left < len(row):
            left = find_next_non_obstacle(left, row)
            right = find_next_obstacle(left, row)
            row[left:right] = sorted(row[left:right], reverse=True)
            left = right + 1
    print(f"box (after) = {box}")
    return rotate(box)

def test(box, expected):
    sol = rotateTheBox(box)
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
    box = [["#",".","#"]]
    expected =  [["."],
                 ["#"],
                 ["#"]]
    test(box, expected)

    
    test_id += 1
    print(f"testcase {test_id}")
    box = [["#",".","*","."],
           ["#","#","*","."]]
    expected = [["#","."],
                ["#","#"],
                ["*","*"],
                [".","."]]
    test(box, expected)
    
    test_id += 1
    print(f"testcase {test_id}")
    box = [["#","#","*",".","*","."],
           ["#","#","#","*",".","."],
           ["#","#","#",".","#","."]]
    expected = [[".","#","#"],
                [".","#","#"],
                ["#","#","*"],
                ["#","*","."],
                ["#",".","*"],
                ["#",".","."]]
    test(box, expected)
