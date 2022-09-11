#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from lcimports import *
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose():
            for r in range(len(matrix)):
                for c in range(r+1, len(matrix[0])):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        def flip():
            for r in range(len(matrix)):
                for c in range(len(matrix[0])//2):
                    matrix[r][c], matrix[r][len(matrix[0])-1-c] = matrix[r][len(matrix[0])-1-c], matrix[r][c]

        transpose()
        flip()
        
# @lc code=end

