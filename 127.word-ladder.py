#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
from lcimports import *
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbours = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                neighbours[pattern].append(word)
        
        visited = set()
        visited.add(beginWord)
        q = [(beginWord, 1)]
        while q:
            curr, chain = q.pop(0)
            for i in range(len(curr)):
                pattern = curr[:i] + '*' + curr[i+1:]
                for word in neighbours[pattern]:
                    if word == endWord:
                        return chain + 1
                    if word not in visited:
                        visited.add(word)
                        q.append((word, chain + 1))
        return 0
        
# @lc code=end

