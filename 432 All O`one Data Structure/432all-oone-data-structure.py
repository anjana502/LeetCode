class Node:
    def __init__(self, key = "", val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class AllOne:

    def __init__(self):
        self.cache = {}
        self.front = Node()
        self.rear = Node()
        self.front.next = self.rear
        self.rear.prev = self.front
    
    def addNode(self, node):
        next1 = self.front.next
        self.front.next = node
        node.next = next1
        node.prev = self.front
        next1.prev = node
    
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def insertNodeFromEnd(self, node):
        self.removeNode(node)
        d = node.val
        temp = self.rear.prev

        while (temp != self.front and temp.val > node.val):
            temp = temp.prev
        
        next1 = temp.next
        temp.next = node
        node.next = next1
        node.prev = temp
        next1.prev = node

    def inc(self, key: str) -> None:
        if (key in self.cache):
            self.cache[key].val += 1
            self.insertNodeFromEnd(self.cache[key])
        else:
            newNode = Node(key, 1)
            self.cache[key] = newNode
            self.addNode(newNode)

    def dec(self, key: str) -> None:
        self.cache[key].val -= 1
        d = self.cache[key].val

        if (d == 0):
            self.removeNode(self.cache[key])
            del self.cache[key]
        else:
            self.insertNodeFromEnd(self.cache[key])

    def getMaxKey(self) -> str:
        if (len(self.cache) == 0):
            return ""
        return (self.rear.prev.key)

    def getMinKey(self) -> str:
        if (len(self.cache) == 0):
            return ""
        return (self.front.next.key)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()