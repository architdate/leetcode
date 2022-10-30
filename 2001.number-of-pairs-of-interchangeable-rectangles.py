#
# @lc app=leetcode id=2001 lang=python3
#
# [2001] Number of Pairs of Interchangeable Rectangles
#
from lcimports import *
# @lc code=start
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        rectangles = Counter([i/j for i, j in rectangles])
        ans = 0
        for r in rectangles:
            if rectangles[r] < 2:
                continue
            ans += (rectangles[r] * (rectangles[r] - 1) // 2)
        return ans
        
        
# @lc code=end

