#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
from lcimports import *
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(intervals)):
            s, e = intervals[i]
            if s > newInterval[1]:
                ans.append(newInterval)
                ans.append(intervals[i])
                newInterval = [inf, inf]
            elif e < newInterval[0]:
                ans.append(intervals[i])
            else:
                newInterval = [min(s, newInterval[0]), max(e, newInterval[1])]
        return ans if newInterval[0] == inf else ans + [newInterval]

# @lc code=end

