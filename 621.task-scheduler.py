#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
from lcimports import *
# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = [(-v, k) for k, v in Counter(tasks).items()]
        heapq.heapify(tasks)
        waiting = []
        time = 0
        while tasks:
            v, t = heapq.heappop(tasks)
            new_f = v + 1
            time += 1
            if new_f != 0:
                waiting.append((t, new_f, time + n))
            if not tasks and waiting:
                time = waiting[0][2]
            while waiting:
                if waiting[0][2] == time:
                    heapq.heappush(tasks, (waiting[0][1], waiting[0][0]))
                    waiting.pop(0)
                else:
                    break
        return time
        
# @lc code=end

