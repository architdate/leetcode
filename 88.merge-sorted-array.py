#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from lcimports import *
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = len(nums1) - 1
        a = m - 1
        b = n - 1
        while a >= 0 and b >= 0:
            if nums1[a] > nums2[b]:
                nums1[p] = nums1[a]
                a -= 1
            else:
                nums1[p] = nums2[b]
                b -= 1
            p -= 1
        if a == -1:
            while b >= 0:
                nums1[p] = nums2[b]
                b -= 1
                p -= 1
        
# @lc code=end

