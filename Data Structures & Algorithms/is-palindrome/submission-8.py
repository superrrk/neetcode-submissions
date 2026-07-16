class Solution:
    def isPalindrome(self, s: str) -> bool:
       # parse the string for alphanumeric characters and lowercase
       # compare if string is equal forward and backwards by checking each char on l and r
       # use 2 pointers to skip any spaces, non-alphanumeric chars 

        l, r = 0, len(s) - 1

       # edge case: if str is less than 1 or 0 char, palindrome 
        if len(s) <= 1:
            return True


        while l < r: 

            # parse the string, skip any spaces/nonalphanumeric 
            while l < r and not s[l].isalnum(): 
                l += 1
            
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True


            
    



























    # parse through the string using a left and r poitner to see if they are the same
    # the whole string must be converted to lowercase
    # and remove all the spaces, so that we are just comparing the letters
    # the letter on the l and r pointer must be the same letter, 
    # return true if this is the case for the whole string
    # false otherwise
    
    # edge caes: if a string is empty, return false

    # brute force approach is to make a copy of the string
    # clean the string by checking for alphanumeric char, (a space is not alphanum)
    # then reverse the new string it to see if they are equal
    
        # cleanedString = ""
        # for character in s: 
        #     if character.isalnum():
        #         cleanedString += character.lower()
        # return cleanedString == cleanedString[::-1]
    # Time O(n): loops through each character n times, where n is the average length of the string s
    # Space O(n): created a new string for each character

        l, r = 0, len(s) - 1
        
        while l < r: 
            # checking if valid char/digit, removing spaces, punctuation, and special chars
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # if they're different letters, immediately return false
            if s[l].lower() != s[r].lower():
                return False
            # keep incrementing, decrementing 
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord("a") <= ord(c) < ord("z") or 
                ord("A") <= ord(c) < ord("Z") or
                ord("0") <= ord(c) < ord("9"))
            

