class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Initialize a value for the results
        fleets = 0

        # Sort the postions in descending order 
        init_sort = sorted(zip(position, speed), reverse = True)
        print(init_sort)

        # Unpack the list of tuples
        position = [position for position, speed in init_sort]
        speed = [speed for position, speed in init_sort]
        
        # Calculate how long it should take each car to make it to the target
        times = [0 for k in position]
        for i in range(0, len(position)):
            time = (target - position[i]) / speed[i]
            times[i] = time

        # Start iterating through the times and add to the stack
        stack = []
        for time in times:
            if len(stack) > 0:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)

        return len(stack) 
        
            
                
                
        return fleets