def findErrorNums(nums):
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
    # (R) Take a concret example, say 10111100, if we subtract 1 from it,
    #     we obtain 10111011, i.e. from the rightmost bit of 1 til the right end
    #     those bits become the NOT of their corresponding bits in the original number.
    #     Consequently, when we take its NOT, and AND with the original number, only
    #     100 left, i.e. the rightmost bit of 1.

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

    # Debug
    #print(f"xor0 = {xor0}")
    #print(f"xor1 = {xor1}")

    # [repeated, missing] is the expected return value
    for j in nums:
        if j == xor0:
            return [xor0, xor1]
        elif j == xor1:
            return [xor1, xor0]


def test():
    n = 0

    n += 1
    print(f"test {n:02d}")
    nums = [2,2]
    expected = [2,1]
    sol = findErrorNums(nums)
    if sol == expected:
        print("Congratulations!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
    print()
    yield None




#public class Solution {
#    public int[] findErrorNums(int[] nums) {
#        int xor = 0, xor0 = 0, xor1 = 0;
#        for (int n: nums)
#            xor ^= n;
#        for (int i = 1; i <= nums.length; i++)
#            xor ^= i;
#        int rightmostbit = xor & ~(xor - 1);
#        for (int n: nums) {
#            if ((n & rightmostbit) != 0)
#                xor1 ^= n;
#            else
#                xor0 ^= n;
#        }
#        for (int i = 1; i <= nums.length; i++) {
#            if ((i & rightmostbit) != 0)
#                xor1 ^= i;
#            else
#                xor0 ^= i;
#        }
#        for (int i = 0; i < nums.length; i++) {
#            if (nums[i] == xor0)
#                return new int[]{xor0, xor1};
#        }
#        return new int[]{xor1, xor0};
#    }
#}

if __name__ == "__main__":
    for _ in test():
        pass


