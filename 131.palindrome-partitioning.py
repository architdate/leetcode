#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from lcimports import *
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        def backtrack(i, left, curr):
            nonlocal partitions
            if i == len(s) and left == "":
                partitions.append(curr)
                return
            if i == len(s):
                return
            left += s[i]
            if left == left[::-1]:
                backtrack(i+1, "", curr + [left])
            backtrack(i+1, left, curr)
        backtrack(0, "", [])
        return partitions

# @lc code=end

