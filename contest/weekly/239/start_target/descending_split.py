#class Solution:
#   def splitString(self, s: str) -> bool:
               
def getMinDistance(nums, target, start):
    if nums[start] == target:
        return 0
    for i in range(1, len(nums)):
        try:
            positive_index = min(start + i, len(nums) - 1)
            if nums[positive_index] == target:
                return i
        except:
            pass
        try:
            positive_index = max(start - i, 0)
            if nums[positive_index] == target:
                return i
        except:
            pass


def test(nums, target, start, expected):
    sol = getMinDistance(nums, target, start)
    if sol == expected :
        print("Congrats!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
    print()



if __name__ == "__main__":
    nums = [1,2,3,4,5]
    target = 5
    start = 3
    expected = 1
    test(nums, target, start, expected)


    nums = [1]
    target = 1
    start = 0
    expected = 0
    test(nums, target, start, expected)


    nums = [2202,9326,1034,4180,1932,8118,7365,7738,6220,3440]
    target = 3440
    start = 0
    expected = 9
    test(nums, target, start, expected)
