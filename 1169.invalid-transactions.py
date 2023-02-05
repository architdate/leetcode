#
# @lc app=leetcode id=1169 lang=python3
#
# [1169] Invalid Transactions
#
from lcimports import *
# @lc code=start
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        r = {}
                
        inv = []        
        for i in transactions:
            split = i.split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            if time not in r:
                r[time] = {
                    name: {city}
                }
            else:
                if name not in r[time]:
                    r[time][name]={city}
                else:
                    r[time][name].add(city)
                    
        
        for i in transactions:
            split = i.split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            
            if amount > 1000:
                inv.append(i)
                continue
            
            for j in range(time-60, time+61):
                if j not in r:
                    continue
                if name not in r[j]:
                    continue
                if len(r[j][name]) > 1 or (list(r[j][name])[0] != city):
                    inv.append(i)
                    break
                                        
        return inv          
        
# @lc code=end

