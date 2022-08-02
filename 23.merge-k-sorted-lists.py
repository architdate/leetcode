#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
import heapq
from typing import *
from lcimports import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(n.val, i) for i, n in enumerate(lists) if n]
        heapq.heapify(heap)
        ans = []
        while heap:
            _, i = heapq.heappop(heap)
            tmp = lists[i]
            lists[i] = tmp.next
            tmp.next = None
            ans.append(tmp)
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        ans.append(None)
        for i in range(len(ans) - 1):
            ans[i].next = ans[i+1]
        return ans[0]
        
        
# @lc code=end

