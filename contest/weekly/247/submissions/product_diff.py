class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        L = sorted(nums)
        return  L[-1]*L[-2] - L[0]*L[1]



counter = 1
def test(nums, expected):
    global counter
    print(f"(Test {counter:02d})")
    sol = maxProductDifference(nums)
    if sol == expected :
        print("Congrats!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
    print()
    counter += 1



if __name__ == "__main__":
    nums = [5,6,2,7,4]
    expected = 34
    test(nums, expected)

    nums = [4,2,5,9,7,4,8]
    expected = 64
    test(nums, expected)
