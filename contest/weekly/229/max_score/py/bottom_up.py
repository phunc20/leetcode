#class Solution:
#    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
def maximumScore(nums, multipliers):
    #def recursive_dp(left, right):
    #    """
    #    left ~ right (both end included)
    #    0 <= left < right <= n-1
    #    """
    #    if (left, right) in memo:
    #        return memo[(left, right)]
    #    n_multiplied = n - (right - left + 1)
    #    remainig_multipliers = multipliers[n_multiplied:]
    #    ## Wrong (when n > m)
    #    #if len(remainig_multipliers) == 2:
    #    #    maximum = max(nums[left]*remainig_multipliers[0] + nums[right]*remainig_multipliers[1],
    #    #                  nums[left]*remainig_multipliers[1] + nums[right]*remainig_multipliers[0])
    #    # Correct: 2 is hard, down to 1.
    #    if len(remainig_multipliers) == 1:
    #        maximum = max(nums[left]*remainig_multipliers[0],
    #                      nums[right]*remainig_multipliers[0])
    #    else:
    #        maximum = max(nums[left]*remainig_multipliers[0] + recursive_dp(left+1, right),
    #                      nums[right]*remainig_multipliers[0] + recursive_dp(left, right-1))
    #    memo[(left, right)] = maximum
    #    #print(f"memo[({left}, {right})] = {maximum}")
    #    return maximum

    #return recursive_dp(0, n-1)
    """
    recursion with memoization too slow, it seems.
    Try bottom-up.
    """
    m = len(multipliers)
    n = len(nums)
    memo = {}
    def bottom_up():
        """
        Filling up memo with all solutions like we did in memo_recursion.py
        """
        #while (0, n-1) not in memo:
        ## This is not a good way to loop

        ## k will represent the number of remaining multipliers.
        for k in range(1, m+1):
            remainig_multipliers = multipliers[-k:]
            n_multiplied = m - k
            n_remaining_nums = n - n_multiplied
            ## Note that [left .. right] should be of length n_remaining_nums, and contiguous, i.e.
            ## including all integers in btw left and right.
            if k == 1:
                ## The following is completely wrong!!
                ## Since in most cases, n > m. When k == 1, we still have left < right, not (l, l).
                #for l in range(n):
                #    memo[(l,l)] = remainig_multipliers[0]*nums[l]
                for left in range(n-n_remaining_nums+1):
                    right = left + n_remaining_nums - 1
                    # N.B. when left = n - n_remaining_nums, right = n - 1, the last index of nums.
                    memo[(left, right)] = max(nums[left]*remainig_multipliers[0],
                                              nums[right]*remainig_multipliers[0])
                    #print(f"k = {k}")
                    #print(f"memo[({left}, {right})] = {memo[(left, right)]}")
            else:
                #for left in range(n):
                ## Wrong: left, right has to run thru all possible combinations.
                #for left in range(n-k+1):
                #    #for right in range(left+k-1):
                #    right = left+k-1
                #    memo[(left, right)] = max(nums[left]*remainig_multipliers[0] + memo[(left+1, right)],
                #                              nums[right]*remainig_multipliers[0] + memo[(left, right-1)])
                ## Similar to above when k == 1, the following is wrong. right is not equal to (left+k-1)
                ## Instead the length (right - left + 1) should be equal to n_remaining_nums
                #for left in range(n-k+1):
                #    #for right in range(left+k-1):
                #    right = left+k-1
                #    memo[(left, right)] = max(nums[left]*remainig_multipliers[0] + memo[(left+1, right)],
                #                              nums[right]*remainig_multipliers[0] + memo[(left, right-1)])
                for left in range(n-n_remaining_nums+1):
                    right = left + n_remaining_nums - 1
                    # N.B. when left = n - n_remaining_nums, right = n - 1, the last index of nums.
                    memo[(left, right)] = max(nums[left]*remainig_multipliers[0] + memo[(left+1, right)],
                                              nums[right]*remainig_multipliers[0] + memo[(left, right-1)])
                    #print(f"k = {k}")
                    #print(f"memo[({left}, {right})] = {memo[(left, right)]}")
    bottom_up()
    return memo[(0, n-1)]


if __name__ == "__main__":
    print("Please go to ./main.py for testing")
