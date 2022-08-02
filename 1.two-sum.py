#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import *
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums): 
            if target - n in hm:
                return [hm[target - n], i]
            hm[n] = i
        
# @lc code=end

