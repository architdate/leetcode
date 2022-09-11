#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#
from lcimports import *
# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        ps, pe = -inf, -inf
        for s, e in intervals:
            if pe > s:
                return False
            ps, pe = s, e
        return True
        
# @lc code=end

