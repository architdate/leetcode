#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
from lcimports import *
# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, amt):
            if amt == 0:
                return 1
            if i >= len(coins) or amt < 0:
                return 0
            return dfs(i, amt - coins[i]) + dfs(i+1, amt)
        return dfs(0, amount)

# @lc code=end