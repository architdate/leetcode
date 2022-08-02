#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
from collections import *
# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        dict1 = Counter(s)
        
        for key, val in dict1.items():
            if val < k:
                return max(self.longestSubstring(sub_string, k) for sub_string in s.split(key))
        
        return len(s)

        
# @lc code=end

