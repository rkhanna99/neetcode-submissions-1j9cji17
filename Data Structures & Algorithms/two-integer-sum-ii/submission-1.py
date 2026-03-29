class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, len(numbers) - 1
        while index1 < index2:
            if numbers[index1] + numbers[index2] > target:
                index2 = index2 - 1
            elif numbers[index1] + numbers[index2] < target:
                index1 = index1 + 1
            else:
                if numbers[index1] != numbers[index2]:
                    break

        return [index1 + 1, index2 + 1]