#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        MIN = - (2**31)
        MAX = (2**31 + 1)
        mul = -1 if x < 0 else 1
        x *= mul
        r = str(x)[::-1]
        if int(r) > MAX or int(r) < MIN:
            return 0
        return int(r) * mul
        
# @lc code=end

