class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_ = float("-inf")
        for i in range(len(nums) // 2):
            pair_sum = nums[i] + nums[-i-1]
            if pair_sum > max_:
                max_ = pair_sum
        return max_


def test(nums, expected):
    sol = minPairSum(nums)
    if sol == expected:
        print("Congratulations!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
    print()

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    print(f"testcase {test_id}")
    nums = [3,5,2,3]
    expected = 7
    test(nums, expected)

    test_id += 1
    print(f"testcase {test_id}")
    nums = [3,5,4,2,4,6]
    expected = 8
    test(nums, expected)
    


