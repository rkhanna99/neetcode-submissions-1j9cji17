class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            # Initialize the pointers for the left subarray and the right subarray
            i = j = 0

            merged = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            # Only one of these loops will run to finish out the remainder of the merge
            while i < len(left):
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged


        def mergeSort(nums):
            # Base case only 1 value in nums
            if len(nums) <= 1:
                return nums

            # Calculate the midpoint
            mid = len(nums) // 2

            # Calculate the left and the right subarrays
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return merge(left, right)

        return mergeSort(nums)
