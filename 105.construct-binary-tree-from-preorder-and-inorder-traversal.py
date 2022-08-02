#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        memo = {v: i for i, v in enumerate(inorder)}
        def dfs(i, in_l, in_r):
            if in_l > in_r:
                return None
            root = TreeNode(preorder[i])
            idx = memo[preorder[i]]
            root.left = dfs(i+1, in_l, idx-1)
            root.right = dfs(i+1+idx-in_l, idx+1, in_r)
            return root
        return dfs(0, 0, len(inorder)-1)

        
# @lc code=end

