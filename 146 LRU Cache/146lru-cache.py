class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.front = Node()
        self.rear = Node()
        self.front.next = self.rear
        self.rear.prev = self.front
        self.cache = {}

    def get(self, key: int) -> int:
        if (key not in self.cache):
            return -1
        
        node = self.cache[key]
        data = node.val

        self.removeNode(node)
        self.addNode(node)

        return data

    def put(self, key: int, value: int) -> None:
        if (key in self.cache):
            node = self.cache[key]
            node.val = value

            self.removeNode(node)
            self.addNode(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node

            self.addNode(new_node)

            if (len(self.cache) > self.capacity):
                to_delete = self.rear.prev
                d = to_delete.key

                self.removeNode(to_delete)

                del self.cache[d]
    
    def addNode(self, node):
        next1 = self.front.next
        self.front.next = node
        node.next = next1
        node.prev = self.front
        next1.prev = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)