#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        memo = {}
        def height(node):
            if not node:
                return 0
            if node in memo:
                return memo[node]
            memo[node] = 1 + max(height(node.left), height(node.right))
            return memo[node]
        
        def dfs(node):
            if not node:
                return True
            return abs(height(node.left) - height(node.right)) <= 1 and dfs(node.left) and dfs(node.right)
        
        return dfs(root)
        
# @lc code=end

