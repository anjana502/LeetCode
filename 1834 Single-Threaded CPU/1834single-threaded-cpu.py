import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        for i in range(n):
            tasks[i].append(i)
        
        tasks.sort()
        curr_time = 0
        i = 0
        q = []
        heapq.heapify(q)
        ls = []

        while (i < n or len(q) != 0):
            if (len(q) == 0 and curr_time < tasks[i][0]):
                curr_time = tasks[i][0]
            
            while (i < n and tasks[i][0] <= curr_time):
                enq_time, proc_time, index = tasks[i]
                heapq.heappush(q, (proc_time, index))
                i += 1
            
            proc_time, index = heapq.heappop(q)
            ls.append(index)
            curr_time += proc_time
        
        return ls