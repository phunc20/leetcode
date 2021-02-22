#class Solution:
#    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
def maximumScore(nums, multipliers):
    """
    Greedy cannot give the best solution.
    Brute force with care = dynamic programming
    """
    m = len(multipliers)
    n = len(nums)
    memo = {}
    def recursive_dp(left, right):
        """
        left ~ right (both end included)
        0 <= left < right <= n-1
        """
        if (left, right) in memo:
            return memo[(left, right)]
        n_multiplied = n - (right - left + 1)
        remainig_multipliers = multipliers[n_multiplied:]
        ## Wrong (when n > m)
        #if len(remainig_multipliers) == 2:
        #    maximum = max(nums[left]*remainig_multipliers[0] + nums[right]*remainig_multipliers[1],
        #                  nums[left]*remainig_multipliers[1] + nums[right]*remainig_multipliers[0])
        # Correct: 2 is hard, down to 1.
        if len(remainig_multipliers) == 1:
            maximum = max(nums[left]*remainig_multipliers[0],
                          nums[right]*remainig_multipliers[0])
        else:
            maximum = max(nums[left]*remainig_multipliers[0] + recursive_dp(left+1, right),
                          nums[right]*remainig_multipliers[0] + recursive_dp(left, right-1))
        memo[(left, right)] = maximum
        #print(f"memo[({left}, {right})] = {maximum}")
        return maximum

    return recursive_dp(0, n-1)


if __name__ == "__main__":
    print("Please go to ./main.py for testing")
