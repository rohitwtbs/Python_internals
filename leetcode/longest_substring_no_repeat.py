# Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substrings.append(s[i:j])
        substrings.sort(key=len,reverse=True)
        return get_longest_string(substrings)

    def get_longest_string(s):
        for i in s:
            if(norepeat(i) == True):
                return len(i)
    
    def norepeat(s):
        frequency = {}
        for i in s:
            if(frequency.get(i,0) => 1):
                return False
            else:
                frequency[i] = frequenct.get(i,0) + 1
        return True


