#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
from lcimports import *
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        curr_idx = 0
        i = 0
        while i < n:
            if curr_idx >= len(flowerbed):
                return False
            if flowerbed[curr_idx] == 1:
                curr_idx += 2
                continue
            if flowerbed[curr_idx] == 0 and len(flowerbed) > curr_idx + 1:
                if flowerbed[curr_idx + 1] != 1:
                    curr_idx += 2
                    i += 1
                else:
                    curr_idx += 1
                continue
            if flowerbed[curr_idx] == 0:
                i += 1
                curr_idx += 2

        return True
        
# @lc code=end

