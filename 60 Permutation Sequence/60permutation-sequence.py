class Solution:
    def nextPermutation(self, ls, k):
        if (k == 1):
            return
        
        index = -1
        i = len(ls) - 1

        while (i > 0):
            if (ls[i] > ls[i - 1]):
                index = (i - 1)
                break
            i -= 1
        
        for i in range(len(ls) - 1, index, -1):
            if (ls[i] > ls[index]):
                ls[i], ls[index] = ls[index], ls[i]
                break
        
        low = index + 1
        high = len(ls) - 1

        while (low < high):
            ls[low], ls[high] = ls[high], ls[low]
            low += 1
            high -= 1
        
        self.nextPermutation(ls, k - 1)
    
    def getPermutation(self, n: int, k: int) -> str:
        ls = [str(i) for i in range(1, n + 1)]

        self.nextPermutation(ls, k)

        s = "".join(ls)

        return s