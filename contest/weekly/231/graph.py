#class Solution:
#    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

# brute force
def countRestrictedPaths(n, edges):
    E = [ e for e in edges if e[0] < e[1] else [e[1], e[0], e[2]]]
    def exist_edge_btw(x, y):
        for e in edges:
            if (x == e[0] and y == e[1]) or (x == e[1] and y == e[0]):
                return True
        else:
            return False
    def distanceToLastNode(x):
        pass
    #L_dist = [[i, distanceToLastNode(i)] for i in range(1, n+1)]
    L_dist = sorted([distanceToLastNode(i), i] for i in range(1, n+1))
    stat = dict()
    def n_paths(L):
        """
        arg:
            L, list
                [distanceToLastNode(i), i]
        return:
            (# legitimate paths to Node n)

        esprit:
            dynamic programming
        """
        somme = 0
        if L in stat:
            return stat[L]
        L_less = [LL for LL in L_dist if LL < L]
        for LL in L_less:
            ind_node = LL[1]
            if exist_edge_btw(1, ind_node):
                somme += n_paths(LL)
        stat[L] = somme
        return somme



    for L in L_dist:
        if L[1] = 1:
            L1 = L
    return n_paths(L1)



def test_case(k, nums, limit, goal, expected):
    print(f"Test case {k:02d}")
    ans = minElements(nums, limit, goal)
    if ans == expected:
        print("Correct.")
    else:
        print(f"Incorrect. ans = {ans}, expected = {expected}")


if __name__ == "__main__":
    k = 1
    nums = [1,-1,1]
    limit = 3
    goal = -4
    expected = 2
    test_case(k, nums, limit, goal, expected)

    k = 2
    nums = [1,-10,9,1]
    limit = 100
    goal = 0
    expected = 1
    test_case(k, nums, limit, goal, expected)

