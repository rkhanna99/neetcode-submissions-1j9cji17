class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We need to figure out which list to search in
        left, right = 0, len(matrix) - 1
        midpoint = (left + right) // 2

        # Iterate through the matrix:
        while left < right:
            greatest_element_left = matrix[left][len(matrix[left]) - 1]
            least_element_right = matrix[right][0]
            if target == greatest_element_left or target == least_element_right:
                return True
            if target >= greatest_element_left and target <= least_element_right:
                left = left + 1
                right = right - 1
            elif target > greatest_element_left and target > least_element_right:
                left = left + 1
            elif target < greatest_element_left and target < least_element_right:
                right = right - 1
        print(left)
        print(right)    
        return self.searchList(matrix[left], target)

        
    def searchList(self, nums: List[int], target: int) -> bool:
        # Setup for binary search of a 1D array
        left, right = 0, len(nums) - 1

        # Start the iteration
        while left <= right:
            midpoint = (left + right) // 2
            if nums[midpoint] == target:
                return True
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint - 1
        
        # Return false cause we weren't able to find the value
        return False
