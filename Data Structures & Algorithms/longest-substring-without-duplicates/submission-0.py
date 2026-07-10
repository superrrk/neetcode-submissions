class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashmap 
        charSet = set()
        l = 0 
        str_length = 0

        for r in range(len(s)):
            while s[r] in charSet: 
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            str_length = max(str_length, r - l + 1)

        return str_length