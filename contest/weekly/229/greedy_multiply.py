#class Solution:
#    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
def maximumScore(nums, multipliers):
    """
    Greedy cannot give the best solution.

    Brute force
    from random import randomint
    def random_pick(H, T):
        k = randomint(0,1)
        if k % 2:
            return H, 0
        else:
            return T, -1
    m = len(multipliers)
    n = len(nums)
    score = 0
    for i in range(m):
        head = nums[0]
        tail = nums[-1]
        # randomly pick one if they are equal
        if head == tail:
            chosen, idx = random_pick(head, tail)
            score += multipliers[i] * chosen
            if idx == 0:
                nums = nums[1:]
            else:
                nums = nums[:-1]
        else:
            multipliers[i]
    """
    def recursive_dp(left, right):
        memo = 





