#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
from lcimports import *
# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.refs = 0
    
    def add(self, word):
        node = self
        node.refs += 1
        for c in word:
            if c in node.children:
                node = node.children[c]
                node.refs += 1
            else:
                node.children[c] = TrieNode()
                node = node.children[c]
                node.refs += 1
        node.is_word = True

    def remove(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add(w)
        ans = []
        visited = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def backtrack(r, c, curr, word):
            nonlocal ans
            if curr.children.get(board[r][c]) is None:
                return
            curr = curr.children[board[r][c]]
            word += board[r][c]
            visited.add((r, c))
            if curr.is_word:
                ans.append(word)
                curr.is_word = False
                root.remove(word)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]) or (nr, nc) in visited:
                    continue
                if curr.children.get(board[nr][nc]) is None or curr.children[board[nr][nc]].refs < 1:
                    continue
                backtrack(nr, nc, curr, word)
            visited.remove((r, c))
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, '')
        return ans
        
# @lc code=end

