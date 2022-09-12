#
# @lc app=leetcode id=1383 lang=python3
#
# [1383] Maximum Performance of a Team
#
from lcimports import *
# @lc code=start
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        combined = sorted(list(zip(speed, efficiency)), key=lambda x: (x[1], x[0]))[::-1]
        heap = [combined[0][0]]
        min_efficiency = combined[0][1]
        s_heap = sum(heap)
        max_performance = min_efficiency * s_heap
        for i in range(1, n):
            if len(heap) == k:
                s_heap -= heapq.heappop(heap)
            s_heap += combined[i][0]
            heapq.heappush(heap, combined[i][0])
            max_performance = max(max_performance, s_heap * combined[i][1])
        return max_performance % (10**9 + 7)
        
# @lc code=end

