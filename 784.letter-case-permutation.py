#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
from lcimports import *
# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(i, curr):
            if i == len(s):
                ans.append(curr)
                return
            if s[i].isalpha():
                backtrack(i+1, curr+s[i].lower())
                backtrack(i+1, curr+s[i].upper())
            else:
                backtrack(i+1, curr+s[i])
        backtrack(0, "")
        return ans
        
# @lc code=end

