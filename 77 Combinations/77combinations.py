class Solution:
    def combinations(self, i, start, n, k, ls, ls1):
        if (i == k):
            ls.append(ls1[:])
            return
        
        for j in range(start, n + 1):
            ls1[i] = j
            self.combinations(i + 1, j + 1, n, k, ls, ls1)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ls1 = [0 for i in range(k)]
        ls = []

        self.combinations(0, 1, n, k, ls, ls1)

        return ls