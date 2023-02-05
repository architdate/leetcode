#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#
from lcimports import *
# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i+1, len(nums)-1):
                if nums[j] == 0:
                    continue
                while k < len(nums) and nums[k] < nums[i] + nums[j]:
                    k += 1
                ans += k - j - 1
        return ans

        
# @lc code=end

