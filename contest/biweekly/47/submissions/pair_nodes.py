class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        D = dict()
        for e in edges:
            e = sorted(e)
            if e in D:
                D[e] += 1
            else:
                D[e] = 1
        return [sum(list(D.values()) > q) for q in queries]

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        D = dict()
        for e in edges:
            e = str(sorted(e))
            if e in D:
                D[e] += 1
            else:
                D[e] = 1
        return [sum(list(D.values()) > q) for q in queries]
