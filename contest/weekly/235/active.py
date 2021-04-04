#class Solution:
#    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
#        pass

def findingUsersActiveMinutes(logs, k):
    D_id_uam = {}
    for id_, m in logs:
        if id_ not in D_id_uam:
            D_id_uam[id_] = {m}
        else:
            D_id_uam[id_].add(m)
    answer = [0]*k
    for i in [len(S) for S in D_id_uam.values()]:
        answer[i-1] += 1
    return answer

def test(logs, k, expected):
    ans = findingUsersActiveMinutes(logs, k)
    if ans == expected:
        print("Congratulations!")
    else:
        print("Almost there.")
        print(f"ans = {ans}")
        print(f"expected = {expected}")

if __name__ == "__main__":
    logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
    k = 5
    expected = [0,2,0,0,0]
    test(logs,k,expected)
    
    logs = [[1,1],[2,2],[2,3]]
    k = 4
    expected = [1,1,0,0]
    test(logs,k,expected)
