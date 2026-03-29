class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret_list = []

        idx_map = {}
        target_map = {}

        for index, value in enumerate(nums):
            # Keep track of the index of each value in nums
            if value not in idx_map.keys():
                idx_map[value] = [index]
            else:
                idx_map[value].append(index)

            # Calculate the value needed to make up the target (target - current number = desired value)
            if value not in target_map.keys():
                target_map[value] = target - value
            else:
                continue

        print(idx_map)
        print(target_map)

        for key, value in target_map.items():
            # Edge case if the key == value
            if (key == value):
                if (len(idx_map[value]) > 1):
                    return [idx_map[key][0], idx_map[key][1]]
                else:
                    print(len(idx_map[value]))
                    continue

            elif value in idx_map.keys():
                return [idx_map[key][-1], idx_map[value][-1]]
