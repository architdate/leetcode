#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from lcimports import *
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
        
# @lc code=end

