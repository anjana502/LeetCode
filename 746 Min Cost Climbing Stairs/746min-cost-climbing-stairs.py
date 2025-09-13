class Solution:
    def minCost(self, cost, ls, i):
        if (i == 0 or i == 1):
            return cost[i]
        
        if (ls[i] != -1):
            return ls[i]
        
        ls[i] = cost[i] + min(self.minCost(cost, ls, i - 1), self.minCost(cost, ls, i - 2))

        return ls[i]
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        ls = [-1 for i in range(n)]

        return min(self.minCost(cost, ls, n - 1), self.minCost(cost, ls, n - 2))