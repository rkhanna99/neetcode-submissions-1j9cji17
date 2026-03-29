class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # First we can combine the arrays and sort
        combined = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)

        # Unpack the list of sorted tuples
        position_sorted, speed_sorted = zip(*combined)

        # Initialize our fleets value
        fleets = 0

        # Convert the tuples to lists
        positions_sorted = list(position_sorted)
        speed_sorted = list(speed_sorted)

        # Calculate the time it takes to reach the destination for each car
        time_array = []
        for i in range(0, len(position)):
            time_needed = (target - positions_sorted[i]) / speed_sorted[i]
            time_array.append(time_needed)

        print(time_array)

        # Create a stack to maintain times of fleets
        stack = []

        for time in time_array:
            if len(stack) > 0:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        
        fleets = len(stack)

        return fleets