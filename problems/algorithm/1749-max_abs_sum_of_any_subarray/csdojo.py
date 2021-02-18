def kadane(L):
    max_current = max_global = L[0]
    for x in L[1:]:
        max_current = max(x, max_current + x)
        if max_current > max_global:
            max_global = max_current
    return max_global

class Solution:
    #def maxAbsoluteSum(self, nums: List[int]) -> int:
    def maxAbsoluteSum(self, nums):
        neg_nums = [-x for x in nums]
        pos = kadane(nums)
        neg = kadane(neg_nums)
        return max(pos, neg)

if __name__ == "__main__":
    s = Solution()
    from cases import cases
    for i, case in enumerate(cases):
        if len(case) < 30:
            print(f"s.maxAbsoluteSum({case}) = {s.maxAbsoluteSum(case)}")
        else:
            print(f"s.maxAbsoluteSum(case[{i}]) = {s.maxAbsoluteSum(case)}")
            pass
