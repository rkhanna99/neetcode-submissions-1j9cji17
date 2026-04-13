class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        seen = set()
        result_map = {}

        # Edge case all numbers are positive
        if nums[0] > 0:
            return result

        for i in range(0, len(nums) - 2):
            # Check if we have already computed the values associated with our value at i
            if nums[i] in seen:
                continue

            # Set the other pointers
            j = i + 1
            k = len(nums) - 1

            # Solve for nums[j] + nums[k] = -nums[i]
            target = -nums[i]

            while j < k:
                curr = nums[j] + nums[k]
                if curr < target:
                    j += 1
                elif curr > target:
                    k -= 1
                else:
                    potential_result = [nums[i], nums[j], nums[k]]

                    key = (nums[i], nums[j], nums[k])

                    if key not in result_map:
                        result.append(potential_result)
                        result_map[key] = 1

                    j += 1
                    k -= 1

            seen.add(nums[i])

        return result


        