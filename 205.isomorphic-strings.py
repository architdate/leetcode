#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
from lcimports import *
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = {}
        used = set()
        for i, v in enumerate(s):
            if v in mapper and t[i] != mapper[v]:
                return False
            if v not in mapper:
                if t[i] in used:
                    return False
                mapper[v] = t[i]
                used.add(t[i])
        return True
        
# @lc code=end

