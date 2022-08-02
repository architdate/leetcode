#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#
from typing import *
# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(zip(position, speed))
        stk = []
        for p, s in ps:
            t = (target - p) / s
            while stk and t >= stk[-1]:
                stk.pop()
            stk.append(t)
        return len(stk)

# @lc code=end

