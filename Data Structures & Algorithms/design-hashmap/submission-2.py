class ListNode:

    # Each Linked List Node will have a Key, Value, and Next pointer
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode(0, 0) for i in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        curr = self.hashmap[self.hash(key)]

        # Iterate through the list of node and remember we have dummy node in the beginning
        while curr.next != None:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
            
        # Not in the list so we add it to the end
        curr.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        curr = self.hashmap[self.hash(key)]

        # Iterate through the list of node and remember we have dummy node in the beginning
        while curr.next != None:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next

        return -1
        

    def remove(self, key: int) -> None:
        curr = self.hashmap[self.hash(key)]

        # Iterate through the list of node and remember we have dummy node in the beginning
        while curr.next != None:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


    # Map key to one of the 10k buckets
    def hash(self, key) -> None:
        return (key % 10000)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)