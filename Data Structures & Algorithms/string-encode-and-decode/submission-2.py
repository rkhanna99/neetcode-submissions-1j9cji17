class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_str = ""

        # Iterate through each string to get the length and use that length as a part of the encoding process
        for s in strs:
            curr_len = str(len(s))
            ret_str += curr_len
            ret_str += '#'
            ret_str += s

        print(ret_str)
        return ret_str


    def decode(self, s: str) -> List[str]:
        strs = []

        s_split = list(s)

        curr_len_str = ""
        index = 0
        while index < len(s_split):
            if s_split[index] != '#':
                curr_len_str += s_split[index]
                index += 1
            else:
                print(curr_len_str)
                print(len(curr_len_str))
                # Convert the curr_len value to an int and loop through starting at the next index
                curr_len = int(curr_len_str)
                curr_str = ""
                index += 1
                while curr_len != 0:
                    curr_str += s_split[index]
                    index += 1
                    curr_len -= 1
                
                strs.append(curr_str)
                print(strs)
                curr_len_str = ""

            

        return strs