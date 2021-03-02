class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        L = [None, None]
        sorted_nums = sorted(nums)
        prev = 0
        for current in sorted_nums:
            if current - prev == 1:
                pass
            elif current - prev == 0:
                L[0] = current
            elif current - prev == 2:
                L[1] = current - 1
            prev = current
        if L[1] == None:
            L[1] = len(nums)
        return L
