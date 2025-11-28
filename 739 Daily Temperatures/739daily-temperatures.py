class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls = [0 for i in range(len(temperatures))]
        s = []

        for i in range(len(temperatures)):
            while (len(s) != 0 and temperatures[i] > temperatures[s[-1]]):
                ls[s[-1]] = (i - s[-1])
                s.pop()
            
            s.append(i)
        
        return ls