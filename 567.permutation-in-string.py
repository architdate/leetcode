#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
from collections import *
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        t = Counter(s1)
        w = Counter(s2[:len(s1)])
        if t == w:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            w[s2[r]] += 1
            w[s2[l]] -= 1
            l += 1
            if w == t:
                return True
        return False
        
# @lc code=end

