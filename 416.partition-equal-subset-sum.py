#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from lcimports import *
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        @lru_cache(None)
        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            return dfs(i+1, target-nums[i]) or dfs(i+1, target)
        return dfs(0, target)
        
# @lc code=end

