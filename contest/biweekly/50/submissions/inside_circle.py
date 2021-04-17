class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # initialize answer with 0's
        answer = [0 for _ in range(len(queries))]
        # brute-force solution
        def is_inside(pt, circle):
            x, y ,r = circle
            u, w = pt
            return (x-u)**2 + (y-w)**2 <= r**2
        #for j, (xj, yj, rj) in enumerate(queries):
        for j, circle_j in enumerate(queries):
            n_insiders = 0
            for pt in points:
                if is_inside(pt, circle_j):
                    n_insiders += 1
            answer[j] = n_insiders
        return answer


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

    test_id += 1
    print(f"testcase {test_id}")
    points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
    expected = [2,3,2,4]
    test(points, queries, expected)

