#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
from lcimports import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return ""
            ans = str(node.val)
            ans += f"({dfs(node.left)})"
            ans += f"({dfs(node.right)})"
            return ans
        ans = dfs(root)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        bracketmap = {}
        stk = []
        for i, v in enumerate(data):
            if v == '(':
                stk.append(i)
                continue
            if v == ')':
                bracketmap[stk.pop()] = i
        
        def dfs(tree, offset):
            if not tree:
                return None
            for i, v in enumerate(tree):
                if v == '(':
                    break
            # i + offset chars before
            root = TreeNode(int(tree[:i]))
            root.right = dfs(tree[bracketmap[i+offset]-offset+2: -1], bracketmap[i+offset]+2)
            root.left = dfs(tree[i+1: bracketmap[i+offset]-offset], i+offset+1)
            return root
            
        return dfs(data, 0)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

