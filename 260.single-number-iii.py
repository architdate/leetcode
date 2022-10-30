#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
from lcimports import *
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask, first = 0, 0
        for n in nums:
            mask ^= n

        bit = mask & -mask
        for n in nums:
            if n & bit:
                first ^= n
        return [first, mask ^ first]
        
# @lc code=end

