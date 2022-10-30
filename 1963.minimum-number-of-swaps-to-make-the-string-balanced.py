#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#
from lcimports import *
import math
# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        close, maxclose = 0, 0
        for c in s:
            if c == '[':
                close -= 1
            else:
                close += 1
            maxclose = max(close, maxclose)
        return math.ceil(maxclose / 2)
        
# @lc code=end

