class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        prev = 0

        for i in range(1, len(points)):
            if (points[i][0] <= points[prev][1]):
                points[prev][1] = min(points[prev][1], points[i][1])
            else:
                count += 1
                prev = i
        
        return count
