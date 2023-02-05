#
# @lc app=leetcode id=723 lang=python3
#
# [723] Candy Crush
#
from lcimports import *
# @lc code=start
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(board), len(board[0])
        def helper():
            changed = False
            flags = [[False]* COLS for _ in range(ROWS)]
            for c in range(COLS):
                for r in range(2, ROWS):
                    if board[r][c] != 0 and board[r][c] == board[r-1][c] == board[r-2][c]:
                        flags[r][c] = flags[r-1][c] = flags[r-2][c] = True
                        changed = True

            for r in range(ROWS):
                for c in range(2, COLS):
                    if board[r][c] != 0 and board[r][c] == board[r][c-1] == board[r][c-2]:
                        flags[r][c] = flags[r][c-1] = flags[r][c-2] = True
                        changed = True

            for c in range(COLS):
                p1, p2 = ROWS - 1, ROWS - 1
                while p2 >= 0:
                    if flags[p2][c] == True:
                        p2 -= 1
                        continue
                    board[p1][c] = board[p2][c]
                    p1 -= 1
                    p2 -= 1
                while p1 >= 0:
                    board[p1][c] = 0
                    p1 -= 1
            return changed
        ch = helper()
        while ch:
            ch = helper()
        return board
                        

        
# @lc code=end

