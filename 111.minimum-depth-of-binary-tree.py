#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = inf
        def backtrack(node, d):
            nonlocal depth
            if not node:
                return
            if not node.left and not node.right:
                depth = min(depth, d)
                return
            backtrack(node.left, d+1)
            backtrack(node.right, d+1)
        backtrack(root, 1)
        return depth if depth != inf else 0
        
# @lc code=end

