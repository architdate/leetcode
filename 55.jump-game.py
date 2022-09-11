#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
from lcimports import *
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        to_reach = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= to_reach:
                to_reach = i
        return to_reach == 0
        
# @lc code=end

