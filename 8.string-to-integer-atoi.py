#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        MAX, MIN = 2 ** 31 - 1, -(2 ** 31)
        sign = -1 if s.startswith('-') else 1
        if s.startswith('-') or s.startswith('+'): s = s[1:]
        res = 0
        for v in s:
            if not v.isdigit():
                break
            if ((res > MAX // 10) or (res == MAX // 10 and int(v) > MAX % 10)):
                return MAX if sign == 1 else MIN
            res = 10 * res + int(v)
        return sign * res
        
# @lc code=end

