#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
from lcimports import *
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        ans = []
        def backtrack(i, k, t, curr):
            if t == 0 and k == 0:
                ans.append(curr)
                return
            if t <= 0 or i >= len(nums) or k <= 0 or nums[i] > t:
                return
            backtrack(i+1, k, t, curr)
            backtrack(i+1, k-1, t-nums[i], curr + [nums[i]])
        backtrack(0, k, n, [])
        return ans

        @lru_cache(None)
        def dfs(i, k, t):
            if t == 0 and k == 0:
                return [[]]
            if t <= 0 or i >= len(nums) or k <= 0 or nums[i] > t:
                return []
            return [[nums[i]] + x for x in dfs(i+1, k-1, t-nums[i])] + dfs(i+1, k, t)
        return dfs(0, k, n)
        
# @lc code=end

