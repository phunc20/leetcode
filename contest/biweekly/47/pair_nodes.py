def countPairs(n, edges, queries):
    #D = dict()
    #for e in edges:
    #    e = sorted(e)
    #    if e in D:
    #        D[e] += 1
    #    else:
    #        D[e] = 1
    #return [sum(list(D.values()) > q) for q in queries]
    D = dict()
    for e in edges:
        e = str(sorted(e))
        if e in D:
            D[e] += 1
        else:
            D[e] = 1
    #return [sum(list(D.values()) > q) for q in queries]
    #print(f"D.values() = {D.values()}")
    return [sum( [count > q for count in D.values()] ) for q in queries]


def test_case(k, n, edges, queries, expected):
    print(f"Test case {k:02d}")
    ans = countPairs(n, edges, queries)
    if ans == expected:
        print("Correct.")
    else:
        print(f"Incorrect. ans = {ans}, expected = {expected}")


if __name__ == "__main__":
    k = 1
    n = 4
    edges = [[1,2],[2,4],[1,3],[2,3],[2,1]]
    queries = [2,3]
    expected = [6,5]
    test_case(k, n, edges, queries, expected)
