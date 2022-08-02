#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from functools import lru_cache
from lcimports import *
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(curr, remaining):
            nonlocal ans
            if not remaining:
                ans.append(curr)
                return
            for i, r in enumerate(remaining):
                backtrack(curr + [r], remaining[:i] + remaining[i+1:])
        backtrack([], nums)
        return ans

        @lru_cache(None)
        def dfs(nums):
            if not nums:
                return [[]]
            ans = []
            for i, n in enumerate(nums):
                ans += [[n] + x for x in dfs(tuple(nums[:i] + nums[i+1:]))]
            return ans
        return dfs(tuple(nums))

        
# @lc code=end

