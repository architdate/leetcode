#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
from lcimports import *
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(r, c):
            board[r][c] = "Y"
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if board[nr][nc] != "O":
                    continue
                dfs(nr, nc)
        def isBorder(r, c):
            if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                return True
            return False
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and isBorder(r, c):
                    ans += 1
                    dfs(r, c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "Y":
                    board[r][c] = "O"
        
# @lc code=end

