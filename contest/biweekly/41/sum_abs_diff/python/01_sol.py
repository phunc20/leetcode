class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #result = [0]*len(nums)
        result = [0]*n
        for i in range(1, n+1):
            result[0] = nums[i] - nums[0]
        for i in range(1, n+1):
        for i in range():
