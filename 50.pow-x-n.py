#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
from lcimports import *
# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return self.myPow(x*x, n//2) * x
        
# @lc code=end

