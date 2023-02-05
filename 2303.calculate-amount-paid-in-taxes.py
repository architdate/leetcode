#
# @lc app=leetcode id=2303 lang=python3
#
# [2303] Calculate Amount Paid in Taxes
#
from lcimports import *
# @lc code=start
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        c = 0
        for t, p in brackets:
            if c >= income:
                break
            ans += (min(t, income) - c) * (p / 100)
            c = t
        return ans
        
# @lc code=end

