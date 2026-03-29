class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize a map and value to hold our capacity
        self.cache = {}
        self.capacity = capacity

        # Set pointers for the Least(left) and Most(right) recently used
        self.LRU, self.MRU = Node(-1 , -1), Node(-1, -1)

        # Make it doubly linked
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU 

    # Helper function to remove a node from a doubly linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Helper function to insert a node at the MRU spot (tail or right)
    def insert(self, node):
        original_prev = self.MRU.prev
        original_prev.next = node
        node.prev = original_prev
        node.next = self.MRU
        self.MRU.prev = node


    def get(self, key: int) -> int:
        # Check if the Key is in the cache
        if key in self.cache:
            # Remove key from cache since we just used a get
            self.remove(self.cache[key])

            # Movie it to the MRU spot
            self.insert(self.cache[key])

            # Return the value
            return self.cache[key].value

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Add the new Node to the cache and move the node to the MRU spot
        if key in self.cache:
            self.remove(self.cache[key])
          
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # We need to evict the LRU Node if it goes over capacity
        if len(self.cache) > self.capacity:
            LRU = self.LRU.next
            # Remove from our Linked List
            self.remove(LRU)
            # Remove from our Dict
            del self.cache[LRU.key]
            


