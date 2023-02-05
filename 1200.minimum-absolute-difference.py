#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#
from lcimports import *
# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        for i in range(1, len(arr)):
            if not ans:
                ans = [[arr[i-1], arr[i]]]
                continue
            if arr[i] - arr[i-1] < ans[0][1] - ans[0][0]:
                ans = [[arr[i-1], arr[i]]]
            elif arr[i] - arr[i-1] == ans[0][1] - ans[0][0]:
                ans.append([arr[i-1], arr[i]])
        return ans
        
# @lc code=end

