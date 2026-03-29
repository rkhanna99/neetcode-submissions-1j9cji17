class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get the frquency of each number
        num_tracker = {}
        for num in nums:
            if num in num_tracker:
                num_tracker[num] = num_tracker[num] + 1
            else:
                num_tracker[num] = 1

        # Sort the keys based on values
        sorted_tracker = dict(sorted(num_tracker.items(), key=lambda item:item[1], reverse=True))

        ret_list = list(sorted_tracker.keys())

        return ret_list[0:k]