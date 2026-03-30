class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = self.hash(key)
        
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        index = self.hash(key)
        
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        
        return False

    # Define our Hashing function    
    def hash(self, key: int) -> int:
        index = key % (10**4)
        return index


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)