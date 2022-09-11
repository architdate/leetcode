#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
from lcimports import *
# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        
        nums = [1] + nums + [1]
        @lru_cache(None)
        def dfs(l, r):
            if l > r:
                return 0
            else:
                final = 0
                for i in range(l, r+1):
                    ans = nums[l-1] * nums[i] * nums[r+1]
                    ans += dfs(l, i-1) + dfs(i+1, r)
                    final = max(ans, final)
                return final
        return dfs(1, len(nums) - 2)
        
# @lc code=end

