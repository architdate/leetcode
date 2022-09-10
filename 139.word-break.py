#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from lcimports import *
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dfs(i):
            if i >= len(s):
                return True
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        return True
            return False
        return dfs(0)
        
# @lc code=end

