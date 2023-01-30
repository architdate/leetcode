#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
from lcimports import *
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        ml = inf
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                ml = min(ml, r - l + 1)
                s -= nums[l]
                l += 1
        return ml if ml != inf else 0
        
# @lc code=end

