#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        orig = x
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        return orig == rev

# @lc code=end

