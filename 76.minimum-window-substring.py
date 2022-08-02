#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from collections import *
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isvalid(window, target):
            for t in target:
                if window.get(t, 0) < target[t]:
                    return False
            return True

        if len(s) < len(t):
            return ""
        t = Counter(t)
        l, w = 0, defaultdict(int)
        minwindow = s + s
        for r, v in enumerate(s):
            w[v] += 1
            while l <= r and isvalid(w, t):
                if r - l + 1 < len(minwindow):
                    minwindow = s[l:r+1]
                w[s[l]] -= 1
                l += 1
        return minwindow if minwindow != s + s else ""

        
# @lc code=end

