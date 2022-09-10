#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
from lcimports import *
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i >= len(cost):
                return 0
            return min(dfs(i+1), dfs(i+2)) + cost[i]
        return min(dfs(0), dfs(1))
        
# @lc code=end

