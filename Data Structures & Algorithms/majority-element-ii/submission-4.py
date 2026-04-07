class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # This is the O(n) runtime with O(n) space solution
        # num_map = {}

        # # Check if the value is already in the map
        # for num in nums:
        #     if num in num_map:
        #         num_map[num] += 1
        #     else:
        #         num_map[num] = 1
        
        # ret_list = []

        # for num in num_map:
        #     if num_map[num] > (len(nums) / 3):
        #         ret_list.append(num)

        # return ret_list

        # This is the O(n) runtime and O(1) space solution
        candidate_1, count_1 = 0, 0
        candidate_2, count_2 = 0, 0

        for num in nums:
            # Check if we already have this candidate
            if num == candidate_1:
                count_1 += 1
                continue
            elif num == candidate_2:
                count_2 += 1
                continue

            # Check if we need a new candidate
            if count_1 == 0:
                candidate_1 = num
                count_1 += 1
                continue
            elif count_2 == 0:
                candidate_2 = num
                count_2 += 1
                continue

            # If the candidate isn't 1 or 2 we decrement the count of both
            if num != candidate_1 or num != candidate_2:
                count_1 -= 1
                count_2 -= 1
                continue

        print(candidate_1)
        print(candidate_2)

        # Get the count of the 2 candidates
        count_1, count_2 = 0, 0
        for num in nums:
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1
        
        if count_1 > (len(nums) / 3) and count_2 > (len(nums) / 3):
            return [candidate_1, candidate_2]
        elif count_1 > (len(nums) / 3):
            return [candidate_1]
        elif count_2 > (len(nums) / 3):
            return [candidate_2]
        else:
            return []

