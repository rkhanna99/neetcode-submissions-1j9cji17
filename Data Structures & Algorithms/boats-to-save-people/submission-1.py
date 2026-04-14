class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0

        # First we sort the weights of the people
        people.sort()

        # Check how many people need a boat of their own (1 persons weight = the limit)
        for i in range(len(people) - 1, -1, -1):
            if people[i] == limit:
                result += 1
                people.pop()
            else:
                break

        left, right = 0, len(people) - 1

        while left <= right:
            curr_weight = people[left] + people[right]
            # Lightest and Heaviest person left can go on boat together
            if curr_weight <= limit:
                left += 1
                right -= 1
            # Heaviest person left needs their own boat
            else:
                right -= 1
                
            result += 1

        return result