#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#
from lcimports import *
# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        maximum = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            ans.append(maximum)
            maximum = max(maximum, arr[i])
        return ans[::-1]
        
        
# @lc code=end

