class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        ls = [float("inf") for i in range(n + 1)]
        ls[0] = 0
        
        for i in range(n):
            sum_thickness = 0
            max_height = 0
            
            for j in range(i, -1, -1):
                w = books[j][0]
                h = books[j][1]
                sum_thickness += w
                
                if (sum_thickness > shelfWidth):
                    break
                
                max_height = max(max_height, h)
                ls[i + 1] = min(ls[i + 1], ls[j] + max_height)
        
        return ls[n]