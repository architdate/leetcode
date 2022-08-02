#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, window, max_size, max_freq = 0, {}, 0, 0
        for r, v in enumerate(s):
            window[v] = window.get(v, 0) + 1
            while r - l + 1 - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            max_size = max(max_size, r - l + 1)
        return max_size
        
# @lc code=end

