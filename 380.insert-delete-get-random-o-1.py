#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
from lcimports import *
# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.hmap[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False
        idx = self.hmap[val]
        lastv = self.lst[-1]
        self.lst[idx] = lastv
        self.hmap[lastv] = idx
        self.lst.pop()
        del self.hmap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

