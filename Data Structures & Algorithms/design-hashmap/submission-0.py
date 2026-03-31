class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [ListNode(0, 0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)

        curr = self.map[index]

        # Check if this key is already there
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
            
        curr.next = ListNode(key, value)


    def get(self, key: int) -> int:
        index = self.hash(key)

        curr = self.map[index]

        # Check if the key is already there
        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next
            
        return -1
        

    def remove(self, key: int) -> None:
        index = self.hash(key)

        curr = self.map[index]

        # Check if the key is already there
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    
    # Define a hash function to emphasize reduced collisions
    def hash(self, key):
        index = key % (10**4)
        return index
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)