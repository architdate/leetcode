#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
from typing import *

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        nl = dummy
        mp = {}
        curr = head
        while curr:
            nl.next = Node(curr.val)
            nl = nl.next
            mp[curr] = nl
            curr = curr.next
        curr = dummy.next
        while head:
            if head.random:
                curr.random = mp[head.random]
            curr, head = curr.next, head.next
        return dummy.next
        
# @lc code=end

