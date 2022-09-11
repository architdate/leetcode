#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from lcimports import *
# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(curr, i):
            if i >= len(nums):
                return 1 if curr == target else 0
            return dfs(curr + nums[i], i+1) + dfs(curr - nums[i], i+1)
        return dfs(0, 0)
        
# @lc code=end

