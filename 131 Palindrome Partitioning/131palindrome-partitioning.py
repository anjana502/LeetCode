class Solution:
    def palindrome(self, s):
        i = 0
        j = len(s) - 1

        while (i < j):
            if (s[i] != s[j]):
                return False
            
            i += 1
            j -= 1
        
        return True

    def partition1(self, i, s, ls, ls1):
        if (i == len(s)):
            ls.append(ls1[:])
            return
        
        for j in range(i + 1, len(s) + 1):
            s1 = s[i: j]

            if (self.palindrome(s1) == True):
                ls1.append(s1)
                self.partition1(j, s, ls, ls1)
                ls1.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        ls = []
        ls1 = []

        self.partition1(0, s, ls, ls1)

        return ls 