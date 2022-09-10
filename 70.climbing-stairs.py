#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
from lcimports import *
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(n):
            if n == 1 or n == 2:
                return n
            return dfs(n-1) + dfs(n-2)
        return dfs(n)
        
# @lc code=end

