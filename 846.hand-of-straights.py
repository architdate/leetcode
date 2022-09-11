#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
from lcimports import *
# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        keys = sorted(count.keys())
        for k in keys:
            if count[k] == 0:
                continue
            ct = count[k]
            for i in range(groupSize):
                count[k+i] -= ct
                if count[k+i] < 0:
                    return False
        return True
        
# @lc code=end

