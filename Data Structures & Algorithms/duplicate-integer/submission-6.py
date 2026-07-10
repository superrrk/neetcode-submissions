class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ''' 
        empty array? - no
        
        hashmap to track which numbers already seen
        
        if a number is already in the hashmap, then we know there's a duplicate
        return true

        checks in constant time because my 
        '''
        seen = set() # number : occurences 
        
        for n in nums:
            if n in seen: 
                return True # duplicate found 
            # add it to my hashmap 
            seen.add(n)
        return False



        