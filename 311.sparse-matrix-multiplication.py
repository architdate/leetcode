#
# @lc app=leetcode id=311 lang=python3
#
# [311] Sparse Matrix Multiplication
#
from lcimports import *
# @lc code=start
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for i, l in enumerate(mat1):
            for j, v in enumerate(l):
                if v == 0:
                    continue
                for k, c in enumerate(mat2[j]):
                    ans[i][k] += v * c
        
        return ans
        
# @lc code=end

