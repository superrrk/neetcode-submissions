class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     # edge cases: 
     # if there's no anagram, just return that word in it sublist 
     # by itself
     # if the list is empty, return the empty string in a sublist of a list

     # initial thoughts? approach is to iterate through the array 
     # make sure the characters have the same length
     # put each letter into a hashmap
     # for each word, if its already in the hashmap for all of the characters
     # then add that to the first sublist
     # create a new sublist for every "anagrams" group

    # brute force apporach is to sort every word 
    # then store every sorted version of a word and store this as the key
    # in the dictionary
    # then add the original word back to the correct bucket (dict key)
    # return the list of values from a dict to a list 

    # what the dict looks like: 
    # result["act"] = ["act", "cat"]
    # ["act": "act", "cat"]
        # result = defaultdict(list)
        # for word in strs: 
        #     sortedString = ''.join(sorted(word))
        #     result[sortedString].append(word)
        # return list(result.values())

# time O(m * n log n)
# sort each word (n log n) for each input string (m)
# space O(n)

# efficient hashmap solution
        result = defaultdict(list)
        for string in strs: 
            count = [0] * 26 # a-z
            
            for c in string:
                count[ord(c) - ord("a")] += 1 # 26 ascii value - 0 = 26, gets u 0-26
                                            # a --> 80 - 80 = 0
            result[tuple(count)].append(string)     # b --> 81 - 80 = 1
        # since count doesn't exist yet, we use 
        # default dict to create empty lists automatically
        # default value is a an empty list []

        # convert to tuple bc in python, lists can't be keys, rn it's a list,
        # so we have to convert it to a tuple
        return list(result.values())

# O(m * n)
# m is the number of strings given
# n is the average length of each string (how many char in each string)
