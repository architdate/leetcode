#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#
from lcimports import *
# @lc code=start
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = (2 ** 31) - 1
        ROWS, COLS = len(rooms), len(rooms[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        gates = []
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    gates.append([r, c, 0])
        while gates:
            r, c, d = gates.pop(0)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if rooms[nr][nc] != INF:
                    continue
                rooms[nr][nc] = d + 1
                gates.append([nr, nc, d + 1])
        
# @lc code=end

