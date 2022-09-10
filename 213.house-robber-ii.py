#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from lcimports import *
# @lc code=start
class Solution:
    def rob1(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):
                return 0
            return max(dfs(i+1), nums[i] + dfs(i+2))
        return dfs(0)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
        
# @lc code=end

