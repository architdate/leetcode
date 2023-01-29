#
# @lc app=leetcode id=1984 lang=python3
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
#
from lcimports import *
# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        minimum = inf
        for i in range(len(nums)-k+1):
            minimum = min(minimum, nums[i+k-1] - nums[i])
        return minimum
        
# @lc code=end

