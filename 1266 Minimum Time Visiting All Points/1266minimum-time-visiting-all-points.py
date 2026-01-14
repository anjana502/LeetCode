class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0

        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            d_x = abs(p2[0] - p1[0])
            d_y = abs(p2[1] - p1[1])
            d = max(d_x, d_y)
            time += d
        
        return time