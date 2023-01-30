#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
from lcimports import *
# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ms = sum([abs(x - y) for y in arr[:k]])
        cs = ms
        mi = 0
        l = 0
        for r in range(k, len(arr)):
            cs -= abs(x - arr[l])
            cs += abs(x - arr[r])
            if cs < ms:
                ms = cs
                mi = l + 1
            l += 1
        return arr[mi:mi+k]
        
# @lc code=end

