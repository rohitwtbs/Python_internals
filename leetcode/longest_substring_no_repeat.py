class Solution:

    def norepeat(self, s):
        frequency = {}
        for char in s:  # Corrected loop variable
            if frequency.get(char, 0) >= 1:
                return False
            else:
                frequency[char] = frequency.get(char, 0) + 1
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        input_string  = s
        # added 256 because only 256 ascii characters are there
        ll = min(256, len(s))
        for length in range(ll, 0, -1): 
            for i in range(ll - length + 1):
                if(self.norepeat(input_string[i:i + length])):
                    return len(input_string[i:i + length])
        return 0