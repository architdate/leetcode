#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
from typing import *
from collections import *
import heapq
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win = [-x for x in nums[:k]]
        heapq.heapify(win)
        curr = Counter(win)
        output = [-win[0]]
        for i in range(k, len(nums)):
            curr[-nums[i-k]] -= 1
            curr[-nums[i]] += 1
            heapq.heappush(win, -nums[i])
            while curr[win[0]] == 0:
                heapq.heappop(win)
            output.append(-win[0])
        return output
        
# @lc code=end

