#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from lcimports import *
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        def twoSum(nums, target):
            start = 0
            end = len(nums) - 1
            ans2 = []
            while start < end:
                if nums[start] + nums[end] == target:
                    ans2.append([nums[start], nums[end]])
                if nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
            return ans2
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                # fixed up i and j
                rest = nums[j+1:]
                nt = target - nums[i] - nums[j]
                vals = twoSum(rest, nt)
                print(i, j, vals)
                for v in vals:
                    ans.add((nums[i], nums[j], v[0], v[1]))
        return [list(x) for x in ans]
        
# @lc code=end

