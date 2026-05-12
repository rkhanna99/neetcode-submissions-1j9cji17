class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize the 2 pointers to be at the end of both valid lists
        left = m - 1
        right = n - 1

        # Pointer to keep track of the insertion
        insert = len(nums1) - 1

        # Start doing the replacement
        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[insert] = nums1[left]
                left -= 1
            else:
                nums1[insert] = nums2[right]
                right -= 1
            insert -= 1

        # Insert any remaining elements
        while left >= 0:
            nums1[insert] = nums1[left]
            left -= 1
            insert -= 1

        while right >= 0:
            nums1[insert] = nums2[right]
            right -= 1
            insert -= 1

    