#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
from lcimports import *
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, curr_sum = 0, 0
        for i in range(len(gas)):
            curr_sum += gas[i] - cost[i]
            if curr_sum < 0:
                start = i + 1
                curr_sum = 0
        return start
        
# @lc code=end

