#
# @lc app=leetcode id=1996 lang=python3
#
# [1996] The Number of Weak Characters in the Game
#
from lcimports import *
# @lc code=start
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        stk = []
        for i in range(len(properties)):
            while stk and stk[-1] < properties[i][1]:
                stk.pop()
                count += 1
            stk.append(properties[i][1])
        return count
        
# @lc code=end

