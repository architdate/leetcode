#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
from lcimports import *
# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            return max(dfs(i+1, j), dfs(i, j+1))
        return dfs(0, 0)
        
# @lc code=end

