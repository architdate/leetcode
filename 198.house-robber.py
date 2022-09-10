#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from lcimports import *
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):
                return 0
            return max(dfs(i+1), nums[i] + dfs(i+2))
        return dfs(0)
        
# @lc code=end

