#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
from lcimports import *
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            return 1 + min(dfs(i+1, j), dfs(i+1, j+1), dfs(i, j+1)) # delete, replace, insert
        return dfs(0, 0)
        
# @lc code=end

