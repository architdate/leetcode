#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True
        if s[0] == s[-1]:
            return self.validPalindrome(s[1:-1])
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]
        
# @lc code=end

