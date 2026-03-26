class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = 0
        
        for i in range(1, len(intervals)):
            if (intervals[i][0] <= intervals[prev][1]):
                intervals[prev][1] = max(intervals[prev][1], intervals[i][1])
            else:
                prev += 1
                intervals[prev] = intervals[i]
        
        intervals = intervals[:prev + 1]
        
        return intervals