class Solution:
    def maximalRectangle1(self, heights):
        stack = []
        n = len(heights)
        max1 = 0

        for i in range(n):
            while (len(stack) != 0 and heights[i] <= heights[stack[-1]]):
                index = stack.pop()
                width = (i - stack[-1] - 1) if (len(stack) != 0) else i
                max1 = max(max1, heights[index] * width)
            
            stack.append(i)
        
        while (len(stack) != 0):
            index = stack.pop()
            width = (n - stack[-1] - 1) if (len(stack) != 0) else n
            max1 = max(max1, heights[index] * width)
        
        return max1
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        heights = [0 for i in range(m)]
        max1 = 0

        for i in range(n):
            for j in range(m):
                if (matrix[i][j] == "1"):
                    heights[j] += 1
                else:
                    heights[j] = 0

            d = self.maximalRectangle1(heights)
            max1 = max(max1, d)
        
        return max1