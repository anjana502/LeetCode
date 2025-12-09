class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ls = []

        for i in range(len(intervals)):
            if (newInterval[1] < intervals[i][0]):
                ls.append(newInterval)
                ls.extend(intervals[i:])

                return ls
            elif (intervals[i][1] < newInterval[0]):
                ls.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        ls.append(newInterval)

        return ls