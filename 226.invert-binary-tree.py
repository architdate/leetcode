#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left, root.right = left, right
        return root
        
# @lc code=end

