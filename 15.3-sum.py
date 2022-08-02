#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import *
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        ans = []
        while i < len(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    curr = nums[j]
                    while j < len(nums) and nums[j] == curr:
                        j += 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
            curr = nums[i]
            while i < len(nums) and nums[i] == curr:
                i += 1
        return ans

# @lc code=end

