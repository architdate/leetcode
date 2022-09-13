#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#
from lcimports import *
# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if len(original) == m*n: 
            for i in range(0, len(original), n): 
                ans.append(original[i:i+n])
        return ans 
        
# @lc code=end

