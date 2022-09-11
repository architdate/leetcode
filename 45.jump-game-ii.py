#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from lcimports import *
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        l = r = 0
        
        farthest = 0
        while r < len(nums)-1:
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            ans += 1
            
        return ans
        
# @lc code=end

