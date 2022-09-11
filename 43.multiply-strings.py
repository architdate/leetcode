#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
from lcimports import *
# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mult_single_digit(idx):
            ans = ''
            carry = 0
            for i in range(len(num1) - 1, -1, -1):
                mult = (int(num1[i]) * int(num2[idx])) + carry
                ans = str(mult % 10) + ans
                carry = mult // 10
            if carry != 0:
                ans = str(carry) + ans
            return int(ans)
        
        multiplier = 1
        finans = 0
        for j in range(len(num2) - 1, -1, -1):
            finans += multiplier * mult_single_digit(j)
            multiplier *= 10
        return str(finans)
        
# @lc code=end

