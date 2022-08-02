#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from typing import *
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r, c, b = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                n = board[row][col]
                if n in r[row] or n in c[col]:
                    return False
                block = (col // 3) + (row // 3) * 3
                if n in b[block]:
                    return False
                r[row].add(n)
                c[col].add(n)
                b[block].add(n)
        return True
        
# @lc code=end

