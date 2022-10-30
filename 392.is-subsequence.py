#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr_idx = 0
        for _, v in enumerate(t):
            if curr_idx == len(s):
                return True
            if s[curr_idx] == v:
                curr_idx += 1
        return curr_idx == len(s)
        
# @lc code=end

