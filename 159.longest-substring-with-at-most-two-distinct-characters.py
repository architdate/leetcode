#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#
from lcimports import *
# @lc code=start
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        used = defaultdict(int)
        l = 0
        ans = 0
        for r, v in enumerate(s):
            used[v] += 1
            while len(used) > 2:
                used[s[l]] -= 1
                if (used[s[l]] == 0):
                    del used[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        
# @lc code=end

