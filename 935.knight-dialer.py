#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#
from lcimports import *
# @lc code=start
class Solution:
    def knightDialer(self, n: int) -> int:
        bound = 10**9 + 7
        paths = {1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],\
                 6:[0,1,7],7:[2,6],8:[1,3],9:[2,4],0:[4,6]} 
        
        @lru_cache(None)
        def dfs(num, n):
            if n == 1:
                return 1
            s = 0
            for i in paths[num]:
                s += dfs(i, n-1) % bound
            return s % bound

        res = 0
        for i in range(10):
            res += dfs(i, n) % bound
        return res % bound
        
# @lc code=end

