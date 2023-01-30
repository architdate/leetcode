#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#
from lcimports import *
# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for c in operations:
            if c.lstrip('-').isnumeric():
                s.append(int(c))
            elif c == "C":
                s.pop()
            elif c == "D":
                s.append(s[-1] * 2)
            else:
                s.append(s[-1] + s[-2])
        return sum(s)
        
# @lc code=end

