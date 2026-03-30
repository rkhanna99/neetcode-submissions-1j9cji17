class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # The max frequency is the length of nums
        freq = [[] for i in range(len(nums) + 1)]

        # Get the count of every value in nums
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for key, value in count.items():
            freq[value].append(key)

        print(count)

        print(freq)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result