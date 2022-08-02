#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
from typing import *
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t.lstrip('-').isnumeric() and t != "-":
                stk.append(int(t))
                continue
            x = stk.pop()
            if t == "+":
                stk[-1] += x
            elif t == "-":
                stk[-1] -= x
            elif t == "*":
                stk[-1] *= x
            else:
                stk[-1] = int(stk[-1] / x)
        return stk[0]
# @lc code=end

