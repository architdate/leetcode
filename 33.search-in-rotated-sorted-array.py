#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import *
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[0]:
                if target <= nums[-1] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if target > nums[mid] or target < nums[0]:
                    l = mid + 1
                else:
                    r = mid
        return l if nums[l] == target else -1
        
# @lc code=end

