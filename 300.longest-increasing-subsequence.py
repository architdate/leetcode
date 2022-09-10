#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from lcimports import *
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # top down no tle (prevents unnecessary ignore current index cases)
        @lru_cache(None)
        def dfs(i):
            ans = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, 1 + dfs(j))
            return ans
        
        maximum = 1
        for i in range(len(nums)):
            # force choose number
            maximum = max(maximum, 1 + dfs(i))
        return maximum
        
        # tle
        @lru_cache(None)
        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if nums[i] > prev:
                return max(1 + dfs(i+1, nums[i]), dfs(i+1, prev))
            return dfs(i+1, prev)
        return dfs(0, -inf)
        
# @lc code=end

