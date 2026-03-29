class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [[timestamp, value]]
        else:
            self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap.keys():
            return ""
        else:
            # Extract the list
            search_list = self.timeMap[key]

            # Binary search on the key to return the desired timestamp
            left, right, pos = 0, len(search_list) - 1, -1

            if timestamp < search_list[0][0]:
                return ""


            while left <= right:
                midpoint = (left + right) // 2

                if timestamp > search_list[midpoint][0]:
                    left = midpoint + 1
                    pos = midpoint
                elif timestamp < search_list[midpoint][0]:
                    right = midpoint - 1
                else:
                    return search_list[midpoint][1]

            return search_list[pos][1]
