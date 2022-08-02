#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
from typing import *
from lcimports import *
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getlongest(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]
        
        longest = s[0]
        for i in range(1, len(s)):
            l1 = getlongest(i-1, i)
            l2 = getlongest(i, i)
            if len(l1) > len(longest):
                longest = l1
            if len(l2) > len(longest):
                longest = l2
        return longest
        
# @lc code=end

