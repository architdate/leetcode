#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
from lcimports import *
# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = []
        intervals.sort()
        for s, e in intervals:
            if h and h[0] <= s:
                heapq.heappop(h)
            heapq.heappush(h, e)
        return len(h)
            
        
# @lc code=end

