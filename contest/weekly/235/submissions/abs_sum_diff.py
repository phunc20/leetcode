class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        modulo = 10**9 + 7
        abs_diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        ans = sum(abs_diff)
        #if len(set(abs_diff)) == 1:
        if ans == 0:
            # i.e. all diff are 0
            return ans
        improvements = [0 for i in range(len(nums1))]
        for i, diff in enumerate(abs_diff):
            if diff == 0:
                pass
            else:
                min_diff = diff
                for j in range(len(nums1)):
                    new_diff = abs(nums1[j] - nums2[i])
                    #improvements[i] = max(diff - new_diff, 0)
                    #if new_diff < abs_diff[i]:
                    if new_diff < min_diff:
                        #improvements[i] = min_diff - new_diff
                        min_diff = new_diff
                improvements[i] = diff - min_diff
        ans -= max(improvements)
        return ans % modulo
