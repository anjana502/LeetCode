class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        sum1 = sum(cardPoints)
        j = 0
        max1 = -1

        for i in range(n):
            sum1 -= cardPoints[i]

            while (j <= i and (i - j + 1) > (n - k)):
                sum1 += cardPoints[j]
                j += 1
            
            if ((i - j + 1) == (n - k)):
                max1 = max(max1, sum1)
        
        return max1