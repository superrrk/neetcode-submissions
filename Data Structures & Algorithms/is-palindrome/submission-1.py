class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s
        # reverse the string 
        # compare if the original and reversed string are the same
        filtered = ''
        for c in s: 
            if c.isalnum():
                filtered += c.lower()
        return filtered[::-1] == filtered
            
        