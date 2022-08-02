#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
from lcimports import *
# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            weight = heapq.heappop(stones) - heapq.heappop(stones)
            if weight:
                heapq.heappush(stones, weight)
        return -stones[0] if stones else 0
        
# @lc code=end

