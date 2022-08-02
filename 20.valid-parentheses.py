#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {')': '(', ']': '[', '}': '{'}
        stk = []
        for _, b in enumerate(s):
            if b not in bmap:
                stk.append(b)
                continue
            if not stk:
                return False
            if bmap[b] != stk[-1]:
                return False
            stk.pop()
        return stk == []
        
# @lc code=end

