#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
from lcimports import *
# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, k, selling):
            if k == 0 or i >= len(prices):
                return 0
            if selling:
                return max(dfs(i+1, k, True), dfs(i+1, k-1, False) + prices[i])
            return max(dfs(i+1, k, False), dfs(i+1, k, True) - prices[i])
        return dfs(0, k, False)
        
# @lc code=end

