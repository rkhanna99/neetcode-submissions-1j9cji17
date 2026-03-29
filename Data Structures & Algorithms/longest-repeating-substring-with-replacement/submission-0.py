class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize a dictionary that will hold the count of our characters
        char_dict = {}

        # Split the string
        str_arr = list(s)

        # Initialize a result value
        result = 0

        # Initialize a left and right pointer for the sliding window
        left = right = 0

        # Start the sliding window process
        while right < len(s) + 1:
            if right == 0:
                char_dict[str_arr[right]] = 1
                result = result + 1
                right = right + 1
            else:
                window_length = right - left 
                max_value = char_dict[max(char_dict, key=char_dict.get)]
                print(char_dict)
                print(f"Window length: {window_length} Max Value: {max_value}")
                if window_length - max_value <= k:
                    # Check if this is the current longest substring 
                    if window_length > result:
                        result = window_length
                    
                    
                    if right < len(s):
                        if str_arr[right] not in char_dict:
                            char_dict[str_arr[right]] = 1
                        else:
                            char_dict[str_arr[right]] = char_dict[str_arr[right]] + 1
                        
                        right += 1
                    else:
                        break
                    
                else:
                    char_dict[str_arr[left]] = char_dict[str_arr[left]] - 1
                    left = left + 1
                    
        print(char_dict)
        return result
        
        