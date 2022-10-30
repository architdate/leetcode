#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
from lcimports import *
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = {0: 1}
        cs, ans = 0, 0
        for _, v in enumerate(nums):
            cs += v
            if cs - k in pref:
                ans += pref[cs-k]
            pref[cs] = pref.get(cs, 0) + 1
        return ans
        
# @lc code=end

