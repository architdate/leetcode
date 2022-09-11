#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from lcimports import *
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, curr_sum, maximum = 0, 0, nums[0]
        for r, v in enumerate(nums):
            curr_sum += v
            maximum = max(maximum, curr_sum)
            if curr_sum < 0:
                l = r + 1
                curr_sum = 0
        return maximum
        
# @lc code=end

