class Solution:
    def get_longest_string(self, substrings):
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            substrings: A list of substrings.

        Returns:
            The length of the longest substring without repeating characters.
        """
        for substring in substrings:  # Corrected loop
            if self.norepeat(substring):  # Corrected function call
                return len(substring)
        return 0

    def norepeat(self, s):
        """
        Checks if a string has no repeating characters.

        Args:
            s: The input string.

        Returns:
            True if the string has no repeating characters, False otherwise.
        """
        frequency = {}
        for char in s:  # Corrected loop variable
            if frequency.get(char, 0) >= 1:
                return False
            else:
                frequency[char] = frequency.get(char, 0) + 1
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring without repeating characters.
        """
        input_string  = s
        for length in range(len(input_string), 0, -1): 
            for i in range(len(input_string) - length + 1):
                if(self.norepeat(input_string[i:i + length])):
                    return len(input_string[i:i + length])
        return 0

        # substrings = []
        # l = min(100, len(s))  # Simplified length calculation
        # for i in range(l):
        #     for j in range(i + 1, len(s) + 1):
        #         substrings.append(s[i:j])
        # substrings.sort(key=len, reverse=True)
        # return self.get_longest_string(substrings)