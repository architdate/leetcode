#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from lcimports import *
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        ans = []
        def backtrack(i, k, curr):
            if k == 0:
                ans.append(curr)
                return
            if i >= len(nums):
                return
            backtrack(i + 1, k - 1, curr + [nums[i]])
            backtrack(i + 1, k, curr)
        backtrack(0, k, [])
        return ans

        @lru_cache(None)
        def dfs(i, k):
            if k == 0:
                return [[]]
            if i == len(nums):
                return []
            ans = [[nums[i]] + x for x in dfs(i + 1, k - 1)] + dfs(i + 1, k)
            return ans
        return dfs(0, k)
        
# @lc code=end

