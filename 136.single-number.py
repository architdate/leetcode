#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
from lcimports import *
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans
        
# @lc code=end

