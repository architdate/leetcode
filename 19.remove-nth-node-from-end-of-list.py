#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
from typing import *
from lcimports import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        curr = head
        ct = 1
        while ct < n:
            curr = curr.next
            ct += 1
        
        while curr.next:
            curr = curr.next
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next
        
# @lc code=end

