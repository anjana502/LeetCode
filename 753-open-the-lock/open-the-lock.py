from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if ("0000" in deadends):
            return -1
        
        q = deque([])
        q.append(("0000", 0))
        s = set()
        s.add("0000")

        while (len(q) != 0):
            code, d = q.popleft()

            if (code == target):
                return d
            
            for i in range(len(code)):
                new_code = code[:i] + str((int(code[i]) + 1) % 10) + code[i + 1:]

                if ((new_code not in deadends) and (new_code not in s)):
                    q.append((new_code, d + 1))
                    s.add((new_code))

                new_code = code[:i] + str((int(code[i]) - 1) % 10) + code[i + 1:]

                if ((new_code not in deadends) and (new_code not in s)):
                    q.append((new_code, d + 1))
                    s.add((new_code))
        
        return -1