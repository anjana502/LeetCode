class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        n = len(rating)

        for i in range(n):
            left_count = sum(j < rating[i] for j in rating[:i])
            right_count = sum(k > rating[i] for k in rating[i + 1:])

            count += (left_count * right_count)
            count += ((i - left_count) * (n - i - 1 - right_count))
        
        return count