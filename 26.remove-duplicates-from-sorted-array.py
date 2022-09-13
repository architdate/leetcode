#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from lcimports import *
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        initcount = len(nums)
        i = 0
        while i < initcount:
            if nums[i] == prev:
                nums.pop(i)
                initcount -= 1
                continue
            prev = nums[i]
            i += 1
        return initcount
        
# @lc code=end

