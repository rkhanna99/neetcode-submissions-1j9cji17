class Solution:

    def encode(self, strs: List[str]) -> str:
        # Get the length of each string
        char_tracker = []
        for s in strs:
            char_tracker.append([len(s), s])
        encoded_str = ""
        for val in char_tracker:
            encoded_str = encoded_str + str(val[0]) + "#" + val[1]
        print(encoded_str)
        return encoded_str         

    def decode(self, s: str) -> List[str]:
        decoded_arr = []
        split_str = list(s)
        index = 0
        while index < len(split_str):
            print(index)
            curr_str = ""
            curr_num_str = ""
            while split_str[index] != "#":
                curr_num_str = curr_num_str + split_str[index]
                index = index + 1
            curr_num = int(curr_num_str)
            start = index + 1
            end = start + curr_num
            curr_str = "".join(split_str[start:end])
            print(curr_str)
            decoded_arr.append(curr_str)
            index = end
            print(index)
        return decoded_arr
