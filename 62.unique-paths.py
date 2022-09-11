#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
from lcimports import *
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [[0, 1], [1, 0]]
        @lru_cache(maxsize=None)
        def dfs(r, c):
            if r == m-1 and c == n-1:
                return 1
            ans = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    ans += dfs(nr, nc)
            return ans
        return dfs(0, 0)
        
# @lc code=end

