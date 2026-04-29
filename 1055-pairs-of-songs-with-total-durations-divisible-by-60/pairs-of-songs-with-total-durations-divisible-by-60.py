class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ls = [0 for i in range(60)]

        for i in time:
            ls[i % 60] += 1
        
        count = 0

        for i in range(31):
            if (i == 0 or i == 30):
                count += (ls[i] * (ls[i] - 1) // 2)
            else:
                count += ls[i] * ls[60 - i]
        
        return count