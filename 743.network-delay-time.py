#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
from lcimports import *
# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)} # [time, end]
        for s, e, t in times:
            adj[s].append([t, e])
        
        recieved = set()
        q = [[0, k]]
        while q:
            time, curr = heapq.heappop(q)
            if curr in recieved:
                continue
            recieved.add(curr)
            if len(recieved) == n:
                return time
            for t, e in adj[curr]:
                if e in recieved:
                    continue
                heapq.heappush(q, [time + t, e])
        return -1
        
# @lc code=end

