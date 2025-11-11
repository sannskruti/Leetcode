class Node:
    def __init__(self, key:int, value:int):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache_dict={}

        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    

    def get(self, key: int) -> int:
        # 1. return -1 if  not found
        # 2. if found, we need to access in O(1)

        if key not in self.cache_dict:
            return -1
        node=self.cache_dict[key]
        self.remove(node) #need to implement 
        self.insert(node) #need to implement
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self.remove(self.cache_dict[key])

        if len(self.cache_dict)==self.capacity:
            lru_node=self.tail.prev
            self.remove(lru_node)
            
        new_node=Node(key,value)
        self.insert(new_node)

    def remove(self, node:Node):
        left=node.prev
        right=node.next
        left.next=right
        right.prev=left

        self.cache_dict.pop(node.key,None)

    def insert (self,node:Node):
        self.cache_dict[node.key]=node
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

       

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)