class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_index = 0
        end_index = len(numbers) - 1

        ret_index = []
        while start_index < end_index:
            if numbers[start_index] + numbers[end_index] == target:
                return [start_index + 1, end_index + 1]
            elif numbers[start_index] + numbers[end_index] > target:
                end_index -= 1
            else:
                start_index += 1

        return [0, 0]