#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
from typing import *
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
        
# @lc code=end

