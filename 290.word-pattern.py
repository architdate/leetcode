#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
from lcimports import *
# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        used = set()
        mapper = {}
        for i, p in enumerate(pattern):
            if p not in mapper:
                if words[i] in used:
                    return False
                mapper[p] = words[i]
                used.add(words[i])
            if p in mapper and words[i] != mapper[p]:
                return False
        return True

        
# @lc code=end

