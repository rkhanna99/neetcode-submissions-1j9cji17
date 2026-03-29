class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret_list = [0 for index in range(0, len(temperatures))]
        for index in range(0, len(temperatures)):
             
            while len(stack) > 0:
                if temperatures[index] > stack[-1][0]:
                    value = stack.pop()
                    ret_list[value[1]] = index - value[1]
                else:
                    break
                    
            stack.append((temperatures[index], index))
        
        return ret_list
            