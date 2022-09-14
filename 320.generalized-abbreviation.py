#
# @lc app=leetcode id=320 lang=python3
#
# [320] Generalized Abbreviation
#
from lcimports import *
# @lc code=start
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        @lru_cache(None)
        def dfs(i, can_abbr):
            if i >= len(word):
                return [""]
            ans = [word[i] + x for x in dfs(i + 1, True)]
            if can_abbr == False:
                return ans
            for j in range(i, len(word)):
                abbr = j - i + 1
                ans += [str(abbr) + x for x in dfs(j + 1, False)]
            return ans
        return dfs(0, True)
        
# @lc code=end

