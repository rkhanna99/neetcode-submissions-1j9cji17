class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_1, count_1 = 0, 0
        candidate_2, count_2 = 0, 0

        # Basically every element votes
        for num in nums:
            # If the number is already one of the candidates
            if num == candidate_1:
                count_1 += 1
                continue
            elif num == candidate_2:
                count_2 += 1
                continue

            # If we have any empty slots
            if count_1 == 0:
                candidate_1 = num
                count_1 += 1
                continue
            elif count_2 == 0:
                candidate_2 = num
                count_2 += 1
                continue

            # If the number is not one of the candidates we decrement the candidate with the smaller count
            count_1 -= 1
            count_2 -= 1

        # Check the frequency of the 2 candidates by traversing the input array once
        total_1 = 0
        total_2 = 0
        for num in nums:
            if num == candidate_1:
                total_1 += 1
            elif num == candidate_2:
                total_2 += 1

        if total_1 > (len(nums) // 3):
            if total_2 > (len(nums) // 3):
                return [candidate_1, candidate_2]
            else:
                return [candidate_1]
        elif total_2 > (len(nums) // 3):
            return [candidate_2]
        else:
            return []



