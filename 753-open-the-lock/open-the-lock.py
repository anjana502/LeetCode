from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([])
        s = set()
        deadends = set(deadends)

        if ("0000" in deadends):
            return -1
        
        q.append(("0000", 0))
        s.add("0000")

        while (len(q) != 0):
            word, d = q.popleft()

            if (word == target):
                return d
            
            for i in range(len(word)):
                new_word = word[:i] + str((int(word[i]) + 1) % 10) + word[i + 1:]

                if ((new_word in s) or (new_word in deadends)):
                    continue
                
                q.append((new_word, d + 1))
                s.add(new_word)
            
            for i in range(len(word)):
                new_word = word[:i] + str((int(word[i]) - 1) % 10) + word[i + 1:]

                if ((new_word in s) or (new_word in deadends)):
                    continue
                
                q.append((new_word, d + 1))
                s.add(new_word)
        
        return -1