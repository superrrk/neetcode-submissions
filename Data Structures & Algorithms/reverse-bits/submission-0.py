class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""

        # check if the bit is at position 1 or 0 
        # reads from r --> l from i = 0
        for i in range(32):
            if n & (1 << i): # logic "and"
                binary += "1"
            else:
                binary += "0"
        
        # reverse the sequence of bits
        res = 0

        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= (1 << i) # logic "or" 
        
        return res
        
