#class Solution:
#    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        
def minElements(nums, limit, goal):
    somme = sum(nums)
    abs_diff = abs(goal - somme)
    return abs_diff // limit + (abs_diff % limit > 0)



def test_case(k, nums, limit, goal, expected):
    print(f"Test case {k:02d}")
    ans = minElements(nums, limit, goal)
    if ans == expected:
        print("Correct.")
    else:
        print(f"Incorrect. ans = {ans}, expected = {expected}")


if __name__ == "__main__":
    k = 1
    nums = [1,-1,1]
    limit = 3
    goal = -4
    expected = 2
    test_case(k, nums, limit, goal, expected)

    k = 2
    nums = [1,-10,9,1]
    limit = 100
    goal = 0
    expected = 1
    test_case(k, nums, limit, goal, expected)

