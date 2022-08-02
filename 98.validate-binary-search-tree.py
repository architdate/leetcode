#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
from lcimports import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(n, l, r):
            if not n:
                return True
            if n.val >= r or n.val <= l:
                return False
            return check(n.left, l, n.val) and check(n.right, n.val, r)
        return check(root, -inf, inf)
        
# @lc code=end

