import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.d = {}
        self.q = []
        heapq.heapify(self.q)

        for i in tasks:
            self.d[i[1]] = [i[0], i[2]]
            heapq.heappush(self.q, (-i[2], -i[1], i[0]))

    def add(self, userId: int, taskId: int, priority: int) -> None:    
        self.d[taskId] = [userId, priority]
        heapq.heappush(self.q, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.d[taskId][1] = newPriority
        heapq.heappush(self.q, (-newPriority, -taskId, self.d[taskId][0]))

    def rmv(self, taskId: int) -> None:
        del self.d[taskId]

    def execTop(self) -> int:
        while (len(self.q) != 0):
            p, t, u = heapq.heappop(self.q)
            p *= -1
            t *= -1

            if (t in self.d and self.d[t] == [u, p]):
                del self.d[t]

                return u
        
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()