from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)

        if (endGene not in bank):
            return -1
        
        q = deque([])
        q.append((startGene, 0))
        s = set()
        s.add(startGene)

        while (len(q) != 0):
            word, d = q.popleft()

            if (word == endGene):
                return d

            for i in range(len(word)):
                for j in "AGCT":
                    newWord = word[:i] + j + word[i + 1:]

                    if ((newWord in s) or (newWord not in bank) or (newWord == word)):
                        continue
                    
                    q.append((newWord, d + 1))
                    s.add(newWord)
        
        return -1