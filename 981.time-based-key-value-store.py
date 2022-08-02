#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
from collections import *
import math
# @lc code=start

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.map[key]
        if not vals or timestamp < vals[0][1]:
            return ""
        if timestamp > vals[-1][1]:
            return vals[-1][0]
        l, r = 0, len(vals) - 1
        while l < r:
            mid = int(math.ceil((l + r) / 2))
            if vals[mid][1] > timestamp:
                r = mid -1
            else:
                l = mid
        return vals[l][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

