#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
from typing import *
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest, window = 0, 0, set()
        for r, v in enumerate(s):
            while v in window:
                window.remove(s[l])
                l += 1
            window.add(v)
            longest = max(longest, r - l + 1)
        return longest

        
# @lc code=end

