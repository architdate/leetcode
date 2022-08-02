#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
from lcimports import *
# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
         self.heap = []
         self.k = k
         for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k and val <= self.heap[0]:
            return self.heap[0]
        if len(self.heap) == self.k:
            heapq.heappop(self.heap)
        heapq.heappush(self.heap, val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

