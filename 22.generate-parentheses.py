#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import *
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(n, open, curr):
            if n == 0:
                ans.append(curr + ')' * open)
                return
            backtrack(n-1, open+1, curr + '(')
            if open > 0:
                backtrack(n, open-1, curr + ')')
        backtrack(n, 0, "")
        return ans
        
# @lc code=end

