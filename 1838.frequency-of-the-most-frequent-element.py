#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#
from lcimports import *
# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        ans = 1
        window = 0
        for r, v in enumerate(nums):
            prev = 0
            if r > 0:
                prev = nums[r-1]
            window += (v - prev) * (r - l)
            while window > k:
                window -= (v - nums[l])
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        
# @lc code=end

