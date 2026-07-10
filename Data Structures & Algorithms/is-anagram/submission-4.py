class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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


        