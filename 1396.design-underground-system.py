#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.current = {}
        self.records = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.current[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prev_st, boarding = self.current[id]
        del self.current[id]
        total, ct = self.records.get((prev_st, stationName), (0, 0))
        total += (t - boarding)
        ct += 1
        self.records[(prev_st, stationName)] = (total, ct)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, ct = self.records[(startStation, endStation)]
        return total / ct


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

