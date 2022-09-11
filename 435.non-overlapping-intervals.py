#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
from lcimports import *
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        ce = - inf
        for s, e in intervals:
            if ce > s:
                ans += 1
                ce = min(ce, e)
                continue
            ce = e
        return ans
        
# @lc code=end

