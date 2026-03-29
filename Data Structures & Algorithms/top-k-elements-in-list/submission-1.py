class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        
        # Get the frequency of each num in nums
        for num in nums:
            if num not in freq_dict.keys():
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1

        # Sort the frequency dict based on the value
        sorted_dict = sorted(freq_dict.items(), key=lambda item:item[1], reverse=True)

        print(sorted_dict)

        ret_list = []
        for value in sorted_dict:
            if k == 0:
                break
            else:
                ret_list.append(value[0])
                k -= 1

        return ret_list