#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
#
from lcimports import *
# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.lst = [""] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        self.lst[idKey-1] = value
        while self.ptr < len(self.lst) and self.lst[self.ptr] != "":
            ans.append(self.lst[self.ptr])
            self.ptr += 1
        return ans
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end

