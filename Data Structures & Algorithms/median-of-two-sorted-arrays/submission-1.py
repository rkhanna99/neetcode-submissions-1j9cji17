class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Determine which of the lists is smaller and larger
        smaller_list, larger_list = nums1, nums2
        if len(nums1) > len(nums2):
            smaller_list = nums2
            larger_list = nums1

        # Determine where the median value should be
        total = (len(smaller_list) + len(larger_list))
        half = total // 2

        # Perform binary search on the smaller list
        small_left, small_right = 0, len(smaller_list) - 1
        while True:
            midpoint_small = (small_left + small_right) // 2
            midpoint_large = half - midpoint_small - 2

            # Check if the largest elements in the left windows are smaller than the smallest elements in the right windows
            smaller_list_left = smaller_list[midpoint_small] if midpoint_small >= 0 else float('-inf')
            smaller_list_right = smaller_list[midpoint_small + 1] if len(smaller_list) > midpoint_small + 1 else float('inf')
            larger_list_left = larger_list[midpoint_large] if midpoint_large >= 0 else float('-inf')
            larger_list_right = larger_list[midpoint_large + 1] if len(larger_list) > midpoint_large + 1 else float('inf')

            # Define the successful case: 
            # Largest element in left window of smaller list is less than smallest element in right window of larger list
            # Largest element in left window of larger list is less than smallest element in right window of smaller list
            if smaller_list_left <= larger_list_right and larger_list_left <= smaller_list_right:
                # Even number of elements
                if total % 2 == 0:
                    median = (max(smaller_list_left, larger_list_left) + min(smaller_list_right, larger_list_right)) / 2
                    return median
                else:
                    return min(smaller_list_right, larger_list_right)

            # Move the pointer if needed
            if smaller_list_left > larger_list_right:
                small_right = midpoint_small - 1
            else:
                small_left = midpoint_small + 1