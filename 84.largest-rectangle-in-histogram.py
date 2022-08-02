#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
from typing import *
from math import inf
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-inf)
        stk = []
        maxarea = 0
        for i, h in enumerate(heights):
            idx = i
            while stk and h < stk[-1][0]:
                prev_h, start_idx = stk.pop()
                idx = start_idx
                maxarea = max(maxarea, prev_h * (i - start_idx))
            stk.append((h, idx))
        return maxarea
        
# @lc code=end

