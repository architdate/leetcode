#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
from lcimports import *
# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [inf] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == inf:
                    continue
                tmpPrices[d] = min(tmpPrices[d], prices[s] + p)
            prices = tmpPrices
        return -1 if prices[dst] == inf else prices[dst]

# @lc code=end

