class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if str lengths are different, edge case: return False, not an anagram
        # check if each string has the same freq of each letter
        # use a hashmap of each string and check if they match
        if len(s) != len(t): 
            return False
        
        letter_s = {}
        letter_t = {}

        for i in range(len(s)):
            letter_s[s[i]] = letter_s.get(s[i], 0) + 1
            letter_t[t[i]] = letter_t.get(t[i], 0) + 1
        
        return letter_s == letter_t

    





















     # both strings need to have the exact same length
        # both strings need to have the same freq of each letters
        '''
        hashmap to store the freq of each letter
        a : 2 
        letter : number of times it appears

        hashmap(s) == hashmap(t) 
        '''

        if len(s) != len(t): 
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
