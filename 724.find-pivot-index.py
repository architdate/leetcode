#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
from lcimports import *
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rs = sum(nums)
        ls = 0
        for i, v in enumerate(nums):
            rs -= v
            if rs == ls:
                return i
            ls += v
        return -1
        
# @lc code=end

