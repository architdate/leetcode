#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from functools import lru_cache
from lcimports import *
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i, curr):
            nonlocal ans
            if i == len(nums):
                ans.append(curr)
                return
            backtrack(i+1, curr)
            backtrack(i+1, curr + [nums[i]])
        backtrack(0, [])
        return ans

        @lru_cache(None)
        def dfs(i):
            if i == len(nums):
                return [[]]
            rest = dfs(i + 1)
            return [[nums[i]] + x for x in rest] + rest
        return dfs(0)
        
# @lc code=end

