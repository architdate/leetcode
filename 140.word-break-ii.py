#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
from lcimports import *
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        @lru_cache(None)
        def dfs(i):
            if i >= len(s):
                return [""]
            curr_ans = []
            for w in wordDict:
                if s[i:].startswith(w):
                    curr_ans += [(w + " " + x).strip() for x in dfs(i+len(w))]
            return curr_ans
        return dfs(0)
        
# @lc code=end

