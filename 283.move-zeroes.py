#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from lcimports import *
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, hi = 0, 0
        while lo < len(nums) and nums[lo] != 0:
            lo += 1
            hi += 1
        while hi < len(nums):
            while lo < len(nums) and nums[lo] != 0:
                lo += 1
            while hi < len(nums) and nums[hi] == 0:
                hi += 1
            if hi >= len(nums) or lo >= len(nums):
                break
            nums[hi], nums[lo] = nums[lo], nums[hi]

        
# @lc code=end

