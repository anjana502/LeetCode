import heapq

class Solution:
    def arrangeWords(self, text: str) -> str:
        ls = text.split(" ")
        q = []
        heapq.heapify(q)

        for i in range(len(ls)):
            heapq.heappush(q, (len(ls[i]), i))
        
        s = ""

        while (len(q) != 0):
            d, i = heapq.heappop(q)
            s = s + " " + ls[i].lower()
        
        s = s[1].upper() + s[2:]

        return s