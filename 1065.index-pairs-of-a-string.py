#
# @lc app=leetcode id=1065 lang=python3
#
# [1065] Index Pairs of a String
#
from lcimports import *
# @lc code=start
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for w in words:
            for i in range(len(text)):
                if text[i:].startswith(w):
                    ans.append([i, i+len(w)-1])
        return sorted(ans)
        
# @lc code=end

