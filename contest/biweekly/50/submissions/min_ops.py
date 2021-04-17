class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            # We make sure each element is strictly greater than its predecessor
            n_ops = 0
            for i in range(1, len(nums)):
                diff = nums[i] - nums[i-1]
                if diff <= 0:
                    n_ops += (-diff) + 1
                    nums[i] = nums[i-1] + 1
        return n_ops


def test(nums, expected):
    sol = minOperations(nums)
    if sol == expected:
        print("Congratulations!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
    print()

if __name__ == "__main__":
    test_id = 0
    
    #print(f"testcase {test_id += 1}")
    test_id += 1
    print(f"testcase {test_id}")
    nums = [1,1,1]
    expected = 3
    test(nums, expected)

    test_id += 1
    print(f"testcase {test_id}")
    nums = [1,5,2,4,1]
    expected = 14
    test(nums, expected)

    test_id += 1
    print(f"testcase {test_id}")
    nums = [8]
    expected = 0
    test(nums, expected)


