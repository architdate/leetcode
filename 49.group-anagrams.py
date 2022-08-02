#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import *
from collections import *
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return d.values()
        
# @lc code=end

