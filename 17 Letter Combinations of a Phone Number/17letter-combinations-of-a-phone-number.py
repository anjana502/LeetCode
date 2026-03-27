class Solution:
    def letterCombinations1(self, n, digits, d):
        if (n == 0):
            return []
        
        prev = self.letterCombinations1(n - 1, digits, d)
        s = d[digits[n - 1]]
        curr = []
        
        if (prev == []):
            curr = list(s)
        
        for i in range(len(prev)):
            for j in range(len(s)):
                s1 = prev[i] + s[j]
                curr.append(s1)
        
        return curr
    
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ls = []
        
        return self.letterCombinations1(len(digits), digits, d)