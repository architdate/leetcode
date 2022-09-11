#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
from lcimports import *
# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        @lru_cache(None)
        def dfs(r, c):
            path = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    path = max(path, 1 + dfs(nr, nc))
            return path
        maximum = 0
        for r in range(ROWS):
            for c in range(COLS):
                maximum = max(maximum, dfs(r, c))
        return maximum
        
# @lc code=end

