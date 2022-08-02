#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import *
import math
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l < r:
            mid = int(math.ceil((l + r) / 2))
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid
        row = l
        l, r = 0, len(matrix[row]) - 1
        while l < r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid
        return matrix[row][l] == target

        
# @lc code=end

