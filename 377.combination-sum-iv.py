#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
from lcimports import *
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(t):
            if t == 0:
                return 1
            ans = 0
            for i in range(len(nums)):
                if nums[i] <= t:
                    ans += dfs(t - nums[i])
            return ans
        return dfs(target)
        
# @lc code=end

