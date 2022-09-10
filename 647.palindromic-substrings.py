#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
from lcimports import *
# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        def getcount(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        count = 1
        for i in range(1, len(s)):
            l1 = getcount(i-1, i)
            l2 = getcount(i, i)
            count += l1 + l2
        return count
        
# @lc code=end

