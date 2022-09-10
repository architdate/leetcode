#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from lcimports import *
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(amt):
            if amt == 0:
                return 0
            ans = inf
            for c in coins:
                if c > amt:
                    continue
                ans = min(ans, 1 + dfs(amt-c))
            return ans
        ans = dfs(amount)
        return ans if ans != inf else -1
                
        
        @lru_cache(None)
        def dfs(i, amt):
            if amt == 0:
                return 0
            if amt < 0 or i >= len(coins):
                return inf
            return min(1 + dfs(i, amt-coins[i]), dfs(i+1, amt))
        ans = dfs(0, amount)
        return ans if ans != inf else -1
        
# @lc code=end

