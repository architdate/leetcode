#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from typing import *
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = [height[0]], [height[-1]]
        for i in range(1, len(height)):
            max_l.append(max(height[i], max_l[-1]))
        for i in range(len(height)-2, -1, -1):
            max_r.append(max(height[i], max_r[-1]))
        max_r = max_r[::-1]
        return sum([min(max_l[i], max_r[i]) - height[i] for i in range(len(height))])
        
# @lc code=end

