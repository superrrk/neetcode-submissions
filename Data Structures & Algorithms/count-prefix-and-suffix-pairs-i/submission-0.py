class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0 

        # check if the word i is a prefix/suffix of word j 
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                w1, w2 = words[i], words[j]
                L = len(w1)
                # check if w1 is a suffix/prefix with python slicing
                if w1 == w2[:L] and w1 == w2[-L:]:
                    res += 1
        return res