#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from lcimports import *
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = min(strs, key=lambda x: len(x))
        count = 0
        for i, c in enumerate(minimum):
            for s in strs:
                if s[i] != c:
                    return minimum[:count]
            count += 1
        return minimum[:count]
        
# @lc code=end

