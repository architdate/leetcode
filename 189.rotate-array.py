#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
from lcimports import *
# @lc code=start
class Solution:
    def reverse(self,A,i,j):
        while i<j:
            A[i],A[j] = A[j],A[i]
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L  = len(nums)
        k %= L
        if k:
            self.reverse( nums , 0 , L-1 )
            self.reverse( nums , 0 , k-1 )
            self.reverse( nums , k , L-1 )
        
# @lc code=end

