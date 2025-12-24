class TrieNode:
    def __init__(self):
        self.d = {}
        self.is_end_of_word = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i in word:
            if (i not in curr.d):
                curr.d[i] = TrieNode()
            
            curr = curr.d[i]
        
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for i in word:
            if (i not in curr.d):
                return False
            
            curr = curr.d[i]
        
        if (curr.is_end_of_word == True):
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in prefix:
            if (i not in curr.d):
                return False
            
            curr = curr.d[i]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)