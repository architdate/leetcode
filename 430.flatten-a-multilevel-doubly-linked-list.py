#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#
from lcimports import *
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        def helper(node):
            if not node.child and not node.next:
                return node
            if not node.child:
                return helper(node.next)
            else:
                nxt = node.next
                end = helper(node.child)
                node.next = node.child
                node.child.prev = node
                node.child = None
                end.next = nxt
                if nxt:
                    nxt.prev = end
                    return helper(nxt)
                else: # last node alr reached
                    return end
        helper(head)
        return head

            
        
# @lc code=end

