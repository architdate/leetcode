#
# @lc app=leetcode id=2002 lang=python3
#
# [2002] Maximum Product of the Length of Two Palindromic Subsequences
#
from lcimports import *
# @lc code=start
class Solution:
    def maxProduct(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i, w1, w2):
            if i >= len(s):
                if w1 == w1[::-1] and w2 == w2[::-1]:
                    return len(w1) * len(w2)
                return 0
            return max(dfs(i+1, w1, w2), dfs(i+1, w1 + s[i], w2), dfs(i+1, w1, w2 + s[i]))
        return dfs(0, "", "")
        
# @lc code=end

