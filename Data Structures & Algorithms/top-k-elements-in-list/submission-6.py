class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Each element can appear at most len(nums) times
        buckets = [[] for i in range(0, len(nums) + 1)]

        # Create a map to keep track of the freqencies of each element
        freq_map = {}

        # Get the frequency of each number
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        for key in freq_map:
            frequency = freq_map[key]

            buckets[frequency].append(key)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

            