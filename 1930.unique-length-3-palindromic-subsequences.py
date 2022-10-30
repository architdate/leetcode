#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#
from lcimports import *
# @lc code=start
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        lm = Counter('')
        rm = Counter(s)
        used = set()
        for i, v in enumerate(s):
            rm[v] -= 1
            for c in lm:
                if f'{c}{v}{c}' in used:
                    continue
                if lm[c] >= 1 and rm[c] >= 1:
                    used.add(f'{c}{v}{c}')
            lm[v] += 1
        return len(used)
            
        
# @lc code=end

