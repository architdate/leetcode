#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
from lcimports import *
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        w = Counter(p)
        c = Counter(s[:len(p)])
        l = 0
        ans = []
        for r in range(len(p), len(s)):
            if (w == c):
                ans.append(l)
            c[s[l]] -= 1
            c[s[r]] += 1
            l += 1
        if (w == c):
            ans.append(l)
        return ans

        
# @lc code=end

