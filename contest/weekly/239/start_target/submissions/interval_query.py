class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        def length(interval):
            return interval[1] - interval[0] + 1
        def h(seq):
            #http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3382369#3382369
            #by unutbu
            return sorted(range(len(seq)), key=seq.__getitem__)
        lengths = [length(interval) for interval in intervals]
        #print(f"lengths = {lengths}")
        sorted_indices = h(lengths)
        #print(f"sorted_indices = {sorted_indices}")
        ans = [-1 for _ in range(len(queries))]
        for i, q in enumerate(queries):
            #for p in range(len(intervals)):
            #    s = sorted_indices[p]
            #    if q in intervals[s]
            for s in sorted_indices:
                #if q in intervals[s]:
                Is = intervals[s]
                if q >= Is[0] and q <= Is[1]:
                    ans[i] = lengths[s]
                    #print(f"i = {i}, s = {s}, q = {q}")
                    break
        return ans



counter = 1
def test(intervals, queries, expected):
    global counter
    print(f"Test {counter:02d}")
    sol = minInterval(intervals, queries)
    if sol == expected :
        print("Congrats!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
    print()
    counter += 1



if __name__ == "__main__":
    intervals = [[1,4],[2,4],[3,6],[4,4]]
    queries = [2,3,4,5]
    expected = [3,3,1,4]
    test(intervals, queries, expected)

    intervals = [[2,3],[2,5],[1,8],[20,25]]
    queries = [2,19,5,22]
    expected = [2,-1,4,6]
    test(intervals, queries, expected)
