#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from lcimports import *
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nummap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        if not digits:
            return ans
        def backtrack(i, curr):
            nonlocal ans
            if i == len(digits):
                ans.append(curr)
                return
            for c in nummap[digits[i]]:
                backtrack(i+1, curr + c)
        backtrack(0, "")
        return ans
        
# @lc code=end

