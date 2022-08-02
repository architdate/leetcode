#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import *
from collections import *
import heapq
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        h = []
        for n, v in nums.items():
            if len(h) == k and h[0][0] < v:
                heapq.heappop(h)
            elif len(h) == k:
                continue
            heapq.heappush(h, (v, n))
        return [x[1] for x in h]
        
# @lc code=end

