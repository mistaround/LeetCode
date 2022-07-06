class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        lookup = Trie()
        for w in words:
            lookup.insert(w)
        root = lookup.root
        ans = []
        
        def dfs(i, j, node, prev):
            if i < 0 or j < 0 or i == m or j == n or board[i][j] == "#" or board[i][j] not in node.children:
                return
            char = board[i][j]
            word = prev + char
            node = node.children[char]
            if node.end:
                ans.append(word)
                node.end = False
            board[i][j] = "#"
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                x = i + dx
                y = j + dy
                dfs(x, y, node, word)
            board[i][j] = char
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        
        return ans
            