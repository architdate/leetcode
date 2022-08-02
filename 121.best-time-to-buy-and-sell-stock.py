#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for r, v in enumerate(prices):
            if v < prices[l]:
                l = r
                continue
            profit = max(profit, v - prices[l])
        return profit
        
# @lc code=end

