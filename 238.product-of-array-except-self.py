#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import *
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(0, len(nums)-1):
            left.append(left[-1] * nums[i])
        for i in range(len(nums)-2, 0, -1):
            nums[i] *= nums[i+1]
        nums.pop(0)
        nums.append(1)
        for i in range(len(nums)):
            nums[i] *= left[i]
        return nums
        
# @lc code=end

