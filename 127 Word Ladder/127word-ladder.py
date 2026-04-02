from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = deque()
        s = set()
        q.append((beginWord, 1))
        s.add((beginWord))

        while (len(q) != 0):
            word, d = q.popleft()

            if (word == endWord):
                return d
            
            for i in range(len(word)):
                for j in range(97, 123):
                    new_word = word[:i] + chr(j) + word[i+1:]

                    if ((new_word == word) or (new_word not in wordList) or (new_word in s)):
                        continue
                    
                    q.append((new_word, d + 1))
                    s.add(new_word)
        
        return 0