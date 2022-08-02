#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
from typing import *
import math
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def gethours(b):
            return int(sum([math.ceil(x / b) for x in piles]))
        l, r = 1, max(piles)
        while l < r:
            print(l, r)
            mid = (l + r) // 2
            if gethours(mid) > h:
                l = mid + 1
            else:
                r = mid
        return l
        
# @lc code=end

