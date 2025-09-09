class Solution:
    def numberOfOnes(self, n):
        count = 0

        while (n != 0):
            n &= (n - 1)
            count += 1
        
        return count

    def countBits(self, n: int) -> List[int]:
        ls = [0]

        for i in range(1, n + 1):
            count = self.numberOfOnes(i)
            ls.append(count)
        
        return ls