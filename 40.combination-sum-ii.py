#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from functools import lru_cache
from lcimports import *
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(i, curr, target):
            if i >= len(candidates) and target != 0:
                return
            if target == 0:
                ans.append(curr)
                return
            if candidates[i] <= target:
                backtrack(i+1, curr + [candidates[i]], target - candidates[i])
            j = i
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            backtrack(j, curr, target)
        backtrack(0, [], target)
        return ans

        @lru_cache(None)
        def dfs(i, target):
            if i >= len(candidates) and target != 0:
                return []
            if target == 0:
                return [[]]
            choose = []
            if candidates[i] <= target:
                choose = [[candidates[i]] + x for x in dfs(i+1, target - candidates[i])]
            j = i
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            not_chosen = dfs(j, target)
            return choose + not_chosen
        return dfs(0, target)
        
# @lc code=end

