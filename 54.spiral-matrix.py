#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from lcimports import *
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def run(l, r, t, b):
            partial = []
            partial += matrix[t][l:r+1]
            if t == b:
                return partial
            for row in range(t+1, b):
                partial.append(matrix[row][r])
            partial += matrix[b][l:r+1][::-1]
            if l == r:
                return partial
            for row in range(b-1, t, -1):
                partial.append(matrix[row][l])
            return partial
        ans = []
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        while l <= r and t <= b:
            ans += run(l, r, t, b)
            l += 1
            r -= 1
            t += 1
            b -= 1
        return ans
        
# @lc code=end

