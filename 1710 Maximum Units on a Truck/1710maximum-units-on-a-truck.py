class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda i: i[1], reverse = True)
        count = 0
        i = 0

        print(boxTypes)

        while (truckSize > 0 and i < len(boxTypes)):
            if (boxTypes[i][0] <= truckSize):
                d = boxTypes[i][0]
                truckSize -= boxTypes[i][0]
            else:
                d = truckSize
                truckSize = 0
            
            count += (d * boxTypes[i][1])
            i += 1
        
        return count