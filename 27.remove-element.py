#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from lcimports import *
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[i], nums[curr] = nums[curr], nums[i]
            curr += 1
        return curr
        
# @lc code=end

