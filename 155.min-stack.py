#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val, val))
        else:
            self.stk.append((val, min(val, self.stk[-1][1])))

    def pop(self) -> None:
        return self.stk.pop()[0]

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

