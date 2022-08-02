#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
from collections import Counter
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        
# @lc code=end

