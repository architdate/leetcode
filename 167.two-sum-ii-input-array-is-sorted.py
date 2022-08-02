#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
from typing import *
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return[l+1, r+1]
            if s < target:
                l += 1
            else:
                r -= 1
                
        
# @lc code=end

