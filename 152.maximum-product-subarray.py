#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
from lcimports import *
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mins, maxes = [], []
        for i, n in enumerate(nums):
            if i == 0:
                mins.append(n)
                maxes.append(n)
                continue
            mins.append(min(nums[i] * mins[i-1], nums[i] * maxes[i-1], nums[i]))
            maxes.append(max(nums[i] * mins[i-1], nums[i] * maxes[i-1], nums[i]))
        return max(maxes)
        
# @lc code=end

