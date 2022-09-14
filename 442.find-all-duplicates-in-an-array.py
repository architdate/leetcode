#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
from lcimports import *
# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1
        return ans
        
# @lc code=end

