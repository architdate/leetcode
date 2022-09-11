#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
from lcimports import *
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        is_col = False
        for r in range(ROWS):
            if matrix[r][0] == 0:
                is_col = True
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for j in range(COLS):
                matrix[0][j] = 0

        if is_col:
            for i in range(ROWS):
                matrix[i][0] = 0
        
        
# @lc code=end

