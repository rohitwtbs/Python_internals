class Solution:
    def get_longest_string(self,s):
        for i in s:
            if(self.norepeat(i) == True):
                return len(i)
        return 0

    def norepeat(self,s):
        frequency = {}
        for i in s:
            if(frequency.get(i,0) >= 1):
                return False
            else:
                frequency[i] = frequency.get(i,0) + 1
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substrings.append(s[i:j])
        substrings.sort(key=len,reverse=True)
        return self.get_longest_string(substrings)


