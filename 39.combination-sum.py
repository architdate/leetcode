#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from functools import lru_cache
from lcimports import *
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i, curr, target):
            nonlocal ans
            if i == len(candidates) and target != 0:
                return
            if target == 0:
                ans.append(curr)
                return
            if target >= candidates[i]:
                backtrack(i, curr + [candidates[i]], target - candidates[i])
            backtrack(i + 1, curr, target)
        backtrack(0, [], target)
        return ans

        @lru_cache(None)
        def dfs(i, target):
            if i == len(candidates) and target != 0:
                return []
            if target == 0:
                return [[]]
            choose = []
            if candidates[i] <= target:
                choose = [[candidates[i]] + x for x in dfs(i, target - candidates[i])]
            not_chosen = dfs(i + 1, target)
            return choose + not_chosen
        return dfs(0, target)

        
# @lc code=end

