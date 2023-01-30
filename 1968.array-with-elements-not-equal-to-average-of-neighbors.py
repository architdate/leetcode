#
# @lc app=leetcode id=1968 lang=python3
#
# [1968] Array With Elements Not Equal to Average of Neighbors
#
from lcimports import *
# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        ls = len(nums)
        l, r = 0, ls - 1
        while len(res) != ls:
            res.append(nums[l])
            l += 1
            if l <= r:
                res.append(nums[r])
                r -= 1
        return res
        
# @lc code=end

