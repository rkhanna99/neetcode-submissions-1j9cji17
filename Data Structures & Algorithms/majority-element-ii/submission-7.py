class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Only 2 elements can appear in a list more than n/3 times
        candidate_1, count_1 = -1000000001, 0
        candidate_2, count_2 = -1000000001, 0

        for num in nums:
            # Check if it matches any of the existing candidates
            if candidate_1 == num:
                count_1 += 1
                continue
            elif candidate_2 == num:
                count_2 += 1
                continue

            # Change the candidate
            if count_1 == 0:
                candidate_1 = num
                count_1 += 1
                continue
            elif count_2 == 0:
                candidate_2 = num
                count_2 += 1
                continue


            # If it doesn't match any of the existing candidates we can decrement both
            count_1 -= 1
            count_2 -= 1

        # Now we have our 2 candidates we can check if they appear at least n/3 times
        count_1, count_2 = 0, 0

        print(candidate_1)
        print(candidate_2)

        for num in nums:
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1
    
        if count_1 > (len(nums) / 3):
            if count_2 > (len(nums) / 3):
                return [candidate_1, candidate_2]
            else:
                return [candidate_1]
        elif count_2 > (len(nums) / 3):
            return [candidate_2]
        else:
            return []


