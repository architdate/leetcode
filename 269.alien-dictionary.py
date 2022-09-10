#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
from lcimports import *
# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        inedges = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        inedges[w2[j]] += 1
                        adj[w1[j]].add(w2[j])
                    break
        
        print(adj, inedges)
        q = [char for char in inedges if inedges[char] == 0]
        order = ""
        while q:
            print(q)
            char = q.pop(0)
            order += char
            for neighbor in adj[char]:
                inedges[neighbor] -= 1
                if inedges[neighbor] == 0:
                    q.append(neighbor)
        return order if len(order) == len(adj) else ""
        
# @lc code=end

