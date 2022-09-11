#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from lcimports import *
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        p_s, p_e = intervals[0]
        for curr in range(1, len(intervals)):
            c_s, c_e = intervals[curr]
            if c_s > p_e:
                ans.append([p_s, p_e])
                p_s, p_e = c_s, c_e
            else:
                p_s, p_e = min(p_s, c_s), max(p_e, c_e)
        ans.append([p_s, p_e])
        return ans

# @lc code=end

