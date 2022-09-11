#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
from lcimports import *
# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @lru_cache(None)
        def dfs(i, j):
            if i == len(s1):
                return s2[j:] == s3[i+j:]
            if j == len(s2):
                return s1[i:] == s3[i+j:]
            ans = False
            if s1[i] == s3[i+j]:
                ans = ans or dfs(i+1, j)
            if s2[j] == s3[i+j]:
                ans = ans or dfs(i, j+1)
            return ans
        return dfs(0, 0)
        
# @lc code=end

