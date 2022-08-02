#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import *
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_ct = 0
        for n in nums:
            if n - 1 in nums:
                continue
            ct = 0
            while n in nums:
                ct += 1
                n += 1
            max_ct = max(max_ct, ct)
        return max_ct
        
# @lc code=end

