#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from lcimports import *
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = Counter(nums)
        maximum = max(nums.values())
        for n in nums:
            if nums[n] == maximum:
                return n
        
# @lc code=end

