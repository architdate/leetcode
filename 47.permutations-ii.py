#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
from lcimports import *
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(nums, curr):
            if not nums:
                ans.append(curr)
                return
            visited = set()
            for i, n in enumerate(nums):
                if n in visited:
                    continue
                visited.add(n)
                backtrack(nums[:i] + nums[i+1:], curr + [nums[i]])
        backtrack(nums, [])
        return ans
        
        @lru_cache(None)
        def dfs(nums):
            if not nums:
                return [[]]
            ans = []
            visited = set()
            for i, n in enumerate(nums):
                if n in visited:
                    continue
                visited.add(n)
                ans += [[n] + x for x in dfs(tuple(nums[:i] + nums[i+1:]))]
            return ans
        return dfs(tuple(nums))
        
# @lc code=end

