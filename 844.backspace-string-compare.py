#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
from lcimports import *
# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for c in s:
            if c == "#" and not stack1:
                continue
            elif c == "#":
                stack1.pop()
            else:
                stack1.append(c)
        for c in t:
            if c == "#" and not stack2:
                continue
            elif c == "#":
                stack2.pop()
            else:
                stack2.append(c)
        return stack1 == stack2
        
# @lc code=end

