#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import *
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = []
        for i, t in enumerate(temperatures):
            while stk and t > temperatures[stk[-1]]:
                idx = stk.pop()
                ans[idx] = i - idx
            stk.append(i)
        return ans
        
# @lc code=end

