#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#
from lcimports import *
# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[0] - x[1])
        
        total = 0
        n = len(costs) // 2
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total
        
# @lc code=end

