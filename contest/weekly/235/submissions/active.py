class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
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

