#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
from lcimports import *
# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            ans = dfs(i+1)
            ans += dfs(i+2) if i+1 < len(s) and int(s[i:i+2]) <= 26 else 0
            return ans
        return dfs(0)
        
# @lc code=end

