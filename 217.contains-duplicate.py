#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from typing import *
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
# @lc code=end

