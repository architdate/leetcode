#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
from lcimports import *
# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
        
# @lc code=end

