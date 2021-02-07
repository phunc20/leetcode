class Solution:
    #def maxAbsoluteSum(self, nums: List[int]) -> int:
    def maxAbsoluteSum(self, nums):
        # Collect all subarrays' sum in the dict `sums`
        # The keys of `sums` are tuples (i, j), where i is the
        # starting index and j the ending index (inclusive).
        sums = {(0, i): sum(nums[:i+1]) for i in range(len(nums))}
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                sums[(i,j)] = sums[(i-1,j)] - nums[i-1]
        abs_sums = [abs(x) for x in sums.values()]
        #print(f"sums = {sums}")
        return max(abs_sums)




if __name__ == "__main__":
    s = Solution()
    #print("s.maxAbsoluteSum([1,-3,2,3,-4]) =", s.maxAbsoluteSum([1,-3,2,3,-4]))
    #print("s.maxAbsoluteSum([2,-5,1,-4,3,-2]) =", s.maxAbsoluteSum([2,-5,1,-4,3,-2]))
    from cases import cases
    for i, case in enumerate(cases):
        if len(case) < 20:
            print(f"s.maxAbsoluteSum({case}) = {s.maxAbsoluteSum(case)}")
        else:
            print(f"s.maxAbsoluteSum(case[{i}]) = {s.maxAbsoluteSum(case)}")
