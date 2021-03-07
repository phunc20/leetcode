#class Solution:
#    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
def nearestValidPoint(x, y, points):
    res = -1
    min_ = 10**5
    for i, point in enumerate(points):
        xi, yi = point
        if xi == x:
            dist = abs(yi - y)
        elif yi == y:
            dist = abs(xi - x)
        else:
            continue
        if dist < min_:
            res = i
            min_ = dist
    return res

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


