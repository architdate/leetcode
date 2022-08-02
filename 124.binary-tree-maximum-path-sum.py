#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
from lcimports import *
from functools import lru_cache
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        
        # return max path sum without split
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # compute max path sum WITH split
            ans = max(ans, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return ans
        
# @lc code=end

