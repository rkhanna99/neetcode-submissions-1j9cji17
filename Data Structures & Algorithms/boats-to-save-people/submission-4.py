class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the people array by weight
        people.sort()

        # Set a left pointer and a pointer to the heaviest person
        left = 0
        right = len(people) - 1

        result = 0

        # Check how many people need their own boats
        while right >= 0:
            if people[right] >= limit:
                result += 1
                right -= 1
            else:
                break

        # Start moving both pointers
        while left <= right:
            curr = people[left] + people[right]
            # Largest person left needs their own boat
            if curr > limit:
                result += 1
                right -= 1
            else:
                right -= 1
                left += 1
                result += 1

        return result
        

