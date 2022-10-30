#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from lcimports import *
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1]]
        for _ in range(1, numRows):
            prev = ans[-1]
            mid = [1]
            for i in range(1, len(prev)):
                mid.append(prev[i] + prev[i-1])
            mid.append(1)
            ans.append(mid)
        return ans

        
# @lc code=end

