class TrieNode:
    def __init__(self):
        self.d = {}
        self.isWord = False

    def addWord(self, word):
        temp = self

        for i in word:
            if (i not in temp.d):
                temp.d[i] = TrieNode()
                
            temp = temp.d[i]
            
        temp.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        n = len(board)
        m = len(board[0])
        s = set()
        s1 = set()

        def dfs(i, j, node, word):
            node = node.d[board[i][j]]
            word += board[i][j]

            if (node.isWord == True):
                s.add(word)
            
            s1.add((i, j))
            ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            for k in ls:
                row = i + k[0]
                col = j + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= m) or ((row, col) in s1) or (board[row][col] not in node.d)):
                    continue
                
                dfs(row, col, node, word)
            
            s1.remove((i, j))
        
        for i in range(n):
            for j in range(m):
                if (board[i][j] in root.d):
                    dfs(i, j, root, "")
        
        ls = list(s)

        return ls