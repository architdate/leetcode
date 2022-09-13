#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
from lcimports import *
# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for n in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + n)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

