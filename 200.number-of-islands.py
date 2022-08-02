#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from lcimports import *
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if (nr, nc) in visited or grid[nr][nc] == "0":
                    continue
                dfs(nr, nc)
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    ans += 1
                    dfs(r, c)
        return ans

# @lc code=end

