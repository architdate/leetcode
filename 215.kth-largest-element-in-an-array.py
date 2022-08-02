#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from lcimports import *
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) == k and heap[0] >= n:
                continue
            if len(heap) == k:
                heapq.heappop(heap)
            heapq.heappush(heap, n)
        return heap[0]
        
# @lc code=end

