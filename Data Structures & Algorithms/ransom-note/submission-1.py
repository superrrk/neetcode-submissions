class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # want to check if all letters of ransomeNote are in magazine
        # use a hashmap to count the freq of each letter
        counts = {}

        # creater a hashmap for each letter in magazine
        for letter in magazine:
            # get the cur value, 
            counts[letter] = counts.get(letter, 0) + 1

        # check in ransomeNote if the char is used already, or if it does
        # not exist in counts
        for char in ransomNote:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1

        return True

        # O(n)


