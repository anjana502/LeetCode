class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ls = list(sorted(zip(indices, sources, targets), key = lambda i: i[0]))
        d = 0
        s2 = s
        
        for i, s1, t in ls:
            if (s[i:].startswith(s1)):
                s2 = s2[:i+d] + t + s2[i+d+len(s1):]
                d += len(t) - len(s1)
        
        return s2