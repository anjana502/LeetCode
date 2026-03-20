class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max1 = 0
        n = len(heights)

        for i in range(n):
            while (len(stack) != 0 and heights[i] < heights[stack[-1]]):
                index = stack.pop()
                w = (i - stack[-1] - 1) if (len(stack) != 0) else i
                max1 = max(max1, w * heights[index])
            
            stack.append(i)
        
        while (len(stack) != 0):
            index = stack.pop()
            w = (n - stack[-1] - 1) if (len(stack) != 0) else n
            max1 = max(max1, w * heights[index])
        
        return max1