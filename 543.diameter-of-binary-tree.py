#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
from functools import lru_cache
from lcimports import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        @lru_cache
        def height(n):
            if not n:
                return 0
            return 1 + max(height(n.left), height(n.right))

        max_diamater = 0
        def diameter(n):
            nonlocal max_diamater
            if not n:
                return 0
            max_diamater = max(max_diamater, diameter(n.right), diameter(n.left), height(n.left) + height(n.right))
            return max_diamater
        
        diameter(root)
        return max_diamater
            
        
# @lc code=end

