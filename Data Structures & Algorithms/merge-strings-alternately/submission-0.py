class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_ptr = 0
        word2_ptr = 0

        result = ""

        while word1_ptr < len(word1) and word2_ptr < len(word2):
            if word1_ptr == word2_ptr:
                result += word1[word1_ptr]
                word1_ptr += 1
            else:
                result += word2[word2_ptr]
                word2_ptr += 1

        if word1_ptr < len(word1):
            result += word1[word1_ptr:]
        elif word2_ptr < len(word2):
            result += word2[word2_ptr:]

        return result