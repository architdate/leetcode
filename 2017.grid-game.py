#
# @lc app=leetcode id=2017 lang=python3
#
# [2017] Grid Game
#
from lcimports import *
# @lc code=start
from copy import deepcopy
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        result = float("inf")
        left, right = 0, sum(grid[0])

        for a, b in zip(grid[0], grid[1]):
            right -= a
            result = min(result, max(left, right))
            left += b
        return result
        
# @lc code=end

