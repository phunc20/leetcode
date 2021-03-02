#class Solution:
#    def findErrorNums(self, nums: List[int]) -> List[int]:
        
def findErrorNums(nums):
    L = [None, None]
    sorted_nums = sorted(nums)
    prev = 0
    for current in sorted_nums:
        if current - prev == 1:
            pass
        elif current - prev == 0:
            L[0] = current
        elif current - prev == 2:
            L[1] = current - 1
        prev = current
    ## Note that current - prev == 2 not guaranteed
    ## to happen, but that current - prev == 0 is
    ## guaranteed to take place.
    if L[1] == None:
        L[1] = len(nums)
    return L

def test(nums, expected):
    your_ans = findErrorNums(nums)
    if your_ans == expected:
        print("Correct.")
    else:
        print(f"Incorrect: your_ans = {your_ans}, expected = {expected}")



if __name__ == "__main__":
    print("Test case 01")
    nums = [1,2,2,4]
    expected = [2,3]
    test(nums, expected)

    print("Test case 02")
    nums = [1,1]
    expected = [1,2]
    test(nums, expected)

    print("Test case 03")
    nums = [2,2]
    expected = [2,1]
    test(nums, expected)

