#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
from lcimports import *
# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dist = p[0]**2 + p[1]**2
            if len(heap) == k and -heap[0][0] <= dist:
                continue
            if len(heap) == k:
                heapq.heappop(heap)
            heapq.heappush(heap, (-dist, p))
        return [x[1] for x in heap]
        
# @lc code=end

