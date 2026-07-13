class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0 

        # check if the word i is a prefix/suffix of word j 
        # the outer loop picks at i 
        # the inner loop picks at i + 1, this checks each pair of i against j exactly once, no duplicates
        # nested loop guarentees i check each pair of i and j exactly once
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                w1, w2 = words[i], words[j]
                # set L to length to the character length of w1
                L = len(w1)
                if w1 == w2[:L] and w1 == w2[-L:]:
                    res += 1

        return res