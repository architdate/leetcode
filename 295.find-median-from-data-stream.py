#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
from lcimports import *
# @lc code=start
class MedianFinder:

    def __init__(self):
        self.smaller = [] # max heap
        self.larger = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smaller, -num)
        if self.larger and -self.smaller[0] > self.larger[0]:
            val = -heapq.heappop(self.smaller)
            other = -heapq.heappop(self.larger)
            heapq.heappush(self.larger, val)
            heapq.heappush(self.smaller, other)
        if len(self.smaller) - len(self.larger) > 1:
            heapq.heappush(self.larger, -heapq.heappop(self.smaller))

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.larger):
            return (-self.smaller[0] + self.larger[0]) / 2
        else:
            return -self.smaller[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

