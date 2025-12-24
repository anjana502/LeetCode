class TrieNode:
    def __init__(self):
        self.d = {}
        self.is_end_of_word = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in word:
            if (i not in curr.d):
                curr.d[i] = TrieNode()

            curr = curr.d[i]

        curr.is_end_of_word = True 

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if (i == len(word)):
                if (curr.is_end_of_word == True):
                    return True
                return False
            
            if (word[i] == "."):
                for j in curr.d:
                    if (dfs(i + 1, curr.d[j]) == True):
                        return True
            else:
                if (word[i] not in curr.d):
                    return False
                
                return dfs(i + 1, curr.d[word[i]])
            
            return False
        
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)