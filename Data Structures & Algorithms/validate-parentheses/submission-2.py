class Solution:
    def isValid(self, s: str) -> bool:
        # create a list for the stack
        stack = []
        # hashmap to map open and closing parentheses 
        closeToOpen = { ")":"(", "]":"[", "}":"{" }

        for c in s: 
            # check if c is a closing parentheses (key) 
            if c in closeToOpen:
                # parentheses match: stack not empty, 
                # last value we added in the stack, match the closing key
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # add open parentheses to the stack 
            else:
                stack.append(c)
        # only true if stack is empty, all values have a open and close
        return True if not stack else False