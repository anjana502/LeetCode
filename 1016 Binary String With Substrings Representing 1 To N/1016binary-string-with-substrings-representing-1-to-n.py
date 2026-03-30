class Solution:
    def queryString(self, s: str, n: int) -> bool:
        d = n.bit_length()
        s1 = set()
        
        def addSubstrings(i):
            for j in range(len(s) - i + 1):
                s1.add(int(s[j: j + i], 2))
        
        for i in range(1, d + 1):
            addSubstrings(i)
        
        print(s1)
        
        curr = 1
        
        while (curr <= n):
            if (curr not in s1):
                return False
            curr += 1
        
        return True