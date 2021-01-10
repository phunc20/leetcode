class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num_i = nums[i]
                num_j = nums[j]
                if num_i + num_j == target:
                    return [i, j]
