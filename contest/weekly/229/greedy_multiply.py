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
        if len(remainig_multipliers) == 2:
            maximum = max(nums[left]*remainig_multipliers[0] + nums[right]*remainig_multipliers[1],
                          nums[left]*remainig_multipliers[1] + nums[right]*remainig_multipliers[0])
        else:
            maximum = max(nums[left]*remainig_multipliers[0] + recursive_dp(left+1, right),
                          nums[right]*remainig_multipliers[0] + recursive_dp(left, right-1))
        memo[(left, right)] = maximum
        return maximum

    return recursive_dp(0, n-1)


if __name__ == "__main__":
    nums = [1,2,3]
    multipliers = [3,2,1]
    ans = maximumScore(nums, multipliers)
    expected = 14
    #print(f"{'Correct' if ans == expected else 'Incorrect'}")
    print(f"{'Correct' if ans == expected else f'Incorrect: ans = {ans}, expected = {expected}'}")

    nums = [-5,-3,-3,-2,7,1]
    multipliers = [-10,-5,3,4,6]
    ans = maximumScore(nums, multipliers)
    expected = 102
    print(f"{'Correct' if ans == expected else f'Incorrect: ans = {ans}, expected = {expected}'}")


