class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            return self.searchList(matrix[0], target)


        # Compare the largest number of the left most list and the smallest number in the right most list since we know it is non-decreasing
        left, right = 0, len(matrix) - 1

        while left <= right:
            midpoint = (right + left) // 2
            if target > matrix[midpoint][-1]:
                left = midpoint + 1
            elif target < matrix[midpoint][0]:
                right = midpoint - 1
            else:
                break

        if not (left <= right):
            return False
        else:
            return self.searchList(matrix[midpoint], target)


    # Essentially Binary Search on a single list
    def searchList(self, row: List[int], target) -> bool:
        left, right = 0, len(row) - 1
        while left <= right:
            midpoint = (right + left) // 2
            if row[midpoint] == target:
                return True
            elif row[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return False
            