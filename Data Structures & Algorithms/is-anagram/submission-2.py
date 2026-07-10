class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        check if s and t have the same number of each character
        using a hashmap to count each letter 
        then, check if the hash maps are equal 
        (if character counts are equal)

        time: O(s+t)
        space: O(1)

        ''' 

        # check for same length strings
        if len(s) != len(t):
            return False

        charS, charT = {}, {}

        for i in range(len(s)):
            charS[s[i]] = 1 + charS.get(s[i], 0)
            charT[t[i]] = 1 + charT.get(t[i], 0)
        for c in charS:
            if charS[c] != charT.get(c, 0):
                return False

        return True


        