import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # First we can sort the array since we know that the largest element is the upper bound of k
        piles = sorted(piles)

        # Set up binary search and initialize a value for k
        left, right = 1, piles[-1]
        k = piles[-1]

        while left <= right:
            midpoint = (left + right) // 2

            # Get the time taken at the midpoint
            time_taken = self.timeTaken(piles, midpoint)

            # Check which index we have to move (if we took to much time then we move the left index forward)
            if time_taken > h:
                left = midpoint + 1
            elif time_taken <= h:
                if midpoint < k:
                    k = midpoint

                right = midpoint - 1
            else:
                break

        return k


            

    # Helper method to calculate how long it would take to eat bananas at a given k
    def timeTaken(self, piles: List[int], k: int) -> int:
        result_list = []
        # Divide each element in piles by k to get the time taken
        for pile in piles:
            curr = math.ceil(pile / k)
            result_list.append(curr)

        # Add all of the elements in the result list to get the time taken
        return sum(result_list)
