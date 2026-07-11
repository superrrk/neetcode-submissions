class Solution:
    def validPalindrome(self, s: str) -> bool:
        # we want a palindrome, look for a any odd counts of a
        # letter to be removed 
        # use two-pointer to check for palindrome
        # skip the left letter, check for reversal string
        # repeat for right letter

        l, r = 0, len(s) - 1

        while l < r: 
            if s[l] != s[r]: 
                # python slicing to skip L and include R
                skipL = s[l + 1 : r + 1]
                # include L, skip R
                skipR = s[l : r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1

        return True

        # s[l : r + 1] = include l through r
        # s[l + 1 : r + 1] = skip l, include through r
        # s[l : r] = include l, skip r


