#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checksame(rn, srn):
            if not rn and not srn:
                return True
            if not rn or not srn:
                return False
            if rn.val != srn.val:
                return False
            return checksame(rn.left, srn.left) and checksame(rn.right, srn.right)

        def dfs(root, subRoot):
            if not root:
                return False
            return checksame(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)
        
# @lc code=end

