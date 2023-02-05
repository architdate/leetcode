#
# @lc app=leetcode id=1583 lang=python3
#
# [1583] Count Unhappy Friends
#
from lcimports import *
# @lc code=start
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        dd = {}
        
        for i,x in pairs:
            dd[i] = set(preferences[i][:preferences[i].index(x)])
            dd[x] = set(preferences[x][:preferences[x].index(i)])
        
        ans = 0
            
        for i in dd:
            for x in dd[i]:
                if i in dd[x]:
                    ans += 1
                    break
        
        return ans
        
# @lc code=end

