# https://leetcode.com/problems/palindrome-number/submissions/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_str = str(x)
            l = len(x_str)
            for left_index in range(l):
                right_index = -1 - left_index
                left = x_str[left_index]
                right = x_str[right_index]
                if right != left:
                    return False
            return True
