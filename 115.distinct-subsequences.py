#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
from lcimports import *
# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            ans = dfs(i+1, j)
            ans += dfs(i+1, j+1) if s[i] == t[j] else 0
            return ans
        return dfs(0, 0)
        
# @lc code=end

