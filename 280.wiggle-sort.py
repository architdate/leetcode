#
# @lc app=leetcode id=280 lang=python3
#
# [280] Wiggle Sort
#
from lcimports import *
# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        less = True
        for i, v in enumerate(nums):
            if i == len(nums) - 1:
                return
            if less and v > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], v
            elif not less and v < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], v
            less = not less
        
# @lc code=end

