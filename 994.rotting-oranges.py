#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
from lcimports import *
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        q = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
        minutes = 0
        while q:
            new_q = []
            while q:
                r, c = q.pop(0)
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        new_q.append([nr, nc])
            if new_q:
                minutes += 1
                q = new_q   
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1 
        return minutes

        
# @lc code=end

