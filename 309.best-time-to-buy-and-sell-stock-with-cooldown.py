#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
from lcimports import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if buying:
                return max(dfs(i+1, True), dfs(i+1, False) - prices[i])
            return max(dfs(i+1, False), dfs(i+2, True) + prices[i])
        return dfs(0, True)
        
# @lc code=end

