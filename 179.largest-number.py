#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
from lcimports import *
# @lc code=start
class Wrapper:
    def __init__(self, val):
        self.val = str(val)
        
    def __lt__(self, other):
        return int(self.val+other.val) < int(other.val+self.val)
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [Wrapper(n) for n in nums]
        nums.sort(reverse=True)
        nums = [n.val for n in nums]
        
        return str(int(''.join(nums)))
        
# @lc code=end

