class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (set(range(n+1)) - set(nums)).pop()

