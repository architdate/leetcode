#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
from functools import lru_cache
from lcimports import *
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(i, curr):
            if i >= len(nums):
                ans.append(curr)
                return
            backtrack(i+1, curr + [nums[i]])
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            backtrack(j, curr)
        backtrack(0, [])
        return ans

        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):
                return [[]]
            ans = [[nums[i]] + x for x in dfs(i + 1)]
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            ans += dfs(j)
            return ans
        return dfs(0)
        
# @lc code=end

