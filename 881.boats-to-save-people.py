#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#
from lcimports import *
# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        ans = 0
        while l <= r:
            ans += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
        return ans
        
        
# @lc code=end

