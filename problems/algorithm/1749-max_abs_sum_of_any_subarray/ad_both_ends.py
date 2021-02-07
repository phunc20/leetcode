class Solution:
    #def maxAbsoluteSum(self, nums: List[int]) -> int:
    def maxAbsoluteSum(self, nums):
        """
        Not so sure if this idea is correct.
        First, we take the entire array.
        Then, we remove the array elements from the right, reaching a maximum absolute sum.
        Finally, we remove the array elements from the left to reach a real maximum abs sum.
        """
        def max_abs_subarray(L):
            """
            arg
              L, list
                len(L) >= 1

            return
              j, int
                where abs(sum(L[:j])) is maximum
              maximum, int
                the absolute max sum
            """
            #j = len(L) - 1
            j = len(L)
            somme = sum(L)
            maximum = abs(somme)
            current_somme = somme
            #for k in range(len(L)-1):
            for k in reversed(range(1, len(L))):
                current_somme = current_somme - L[k]
                current_abs = abs(current_somme)
                if current_abs > maximum:
                    j = k
                    maximum = current_abs
            return j, maximum
        #sums = {(0, i): sum(nums[:i+1]) for i in range(len(nums))}
        #right_reduced = nums[:max_abs_subarray(nums)[0]]
        #print(f"right_reduced = {right_reduced}")
        #print(f"sum: {sum(right_reduced)}")
        #print(f"abs sum: {abs(sum(right_reduced))}")
        #return max_abs_subarray(right_reduced)[1]
        right = max_abs_subarray(list(reversed(nums[:max_abs_subarray(nums)[0]])))[1]
        reverse = list(reversed(nums))
        left = max_abs_subarray(list(reversed(reverse[:max_abs_subarray(reverse)[0]])))[1]
        return max(right, left)




if __name__ == "__main__":
    s = Solution()
    #print("s.maxAbsoluteSum([1,-3,2,3,-4]) =", s.maxAbsoluteSum([1,-3,2,3,-4]))
    #print("s.maxAbsoluteSum([2,-5,1,-4,3,-2]) =", s.maxAbsoluteSum([2,-5,1,-4,3,-2]))
    from cases import cases
    for i, case in enumerate(cases):
        if len(case) < 30:
            print(f"s.maxAbsoluteSum({case}) = {s.maxAbsoluteSum(case)}")
        else:
            print(f"s.maxAbsoluteSum(case[{i}]) = {s.maxAbsoluteSum(case)}")
            pass
