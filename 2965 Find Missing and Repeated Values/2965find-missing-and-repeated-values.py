class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ls = [0 for i in range(len(grid) ** 2 + 1)]

        for i in grid:
            for j in i:
                ls[j] += 1
        
        ls1 = [0, 0]

        for i in range(1, len(ls)):
            if (ls[i] > 1):
                ls1[0] = i
            elif (ls[i] == 0):
                ls1[1] = i
        
        return ls1