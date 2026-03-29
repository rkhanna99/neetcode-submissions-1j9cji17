class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [[timestamp, value]]
        else:
            self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # Check if the key is in the timeMap
        if key not in self.timeMap:
            return ""
        else:
            entries = self.timeMap[key]
            left, right, pos = 0, len(entries) - 1, -1
            # Check if the desired timestamp is less than the first timestamp
            if timestamp < entries[0][0]:
                return ""
            # Start the binary search iteration
            while left <= right:
                # Calculate the midpoint
                midpoint = (left + right) // 2

                # Check if the midpoint is the desired timestamp
                if entries[midpoint][0] == timestamp:
                    return entries[midpoint][1]
                
                if entries[midpoint][0] < timestamp:
                    left = midpoint + 1
                    pos = midpoint
                else:
                    right = midpoint - 1

            # Return the left pointer cause we know that will be the closest value <= to timestamp
            return entries[pos][1]
                

        
