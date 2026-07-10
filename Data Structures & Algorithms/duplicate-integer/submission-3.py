class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        use a hashMap to check for a frequency map (if a 
        number repeats itself), then return true, otherwise
        return false

        Time: O(n)
        Space: O(n)

        '''
        hashset = set()
        for n in nums: 
            if n in hashset: 
                return True
            hashset.add(n)
        return False
        