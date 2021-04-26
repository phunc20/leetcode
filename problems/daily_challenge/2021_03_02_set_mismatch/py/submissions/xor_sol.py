class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor = 0
        # n ^ n equals 0 for all integers n.
        # Because ^ is commutative, the order in which the members appear in the sum
        # does not matter.
        for i, n in enumerate(nums):
            j = i + 1
            xor ^= j
            xor ^= n
        # xor now equals (missing ^ repeated)

        # Now, find the rightmost bit on which missing and repeated disagree
        rightmostbit = xor & ~(xor - 1)
        # (?) Why this works?

        # Divide nums into two subsets:
        # one with rightmost bit = 0, the other with rightmost bit = 1
        # Do the same for the set of integers [1..n]
        # Compute the xor of all elements the two subsets with rightmost bit = 0, and assign it to xor0
        # The same for xor1
        xor0 = 0
        xor1 = 0
        for i, n in enumerate(nums):
            j = i + 1
            if n & rightmostbit:
                xor1 ^= n
            else:
                xor0 ^= n
            if j & rightmostbit:
                xor1 ^= j
            else:
                xor0 ^= j

        for j in nums:
            if j == xor0:
                return [xor0, xor1]
            elif j == xor1:
                return [xor1, xor0]



