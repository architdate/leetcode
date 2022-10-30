#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
from lcimports import *
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        for i, v in enumerate(nums):
            if v != 0:
                continue
            nums[i], nums[start] = nums[start], nums[i]
            start += 1
        for i in range(start, len(nums)):
            if nums[i] != 1:
                continue
            nums[i], nums[start] = nums[start], nums[i]
            start += 1
        
# @lc code=end

