#
# @lc app=leetcode id=1387 lang=python3
#
# [1387] Sort Integers by The Power Value
#
from lcimports import *
# @lc code=start
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = {}
        def dfs(n):
            if n in res:
                return res[n]
            c = 0
            t = n
            while t != 1:
                if t % 2 == 0:
                    t //= 2
                else:
                    t = (3 * t) + 1
                c += 1
            res[n] = c
            return c
        for i in range(lo, hi + 1):
            dfs(i)
        return sorted(range(lo, hi + 1), key = lambda x: res[x])[k-1]
        
# @lc code=end

