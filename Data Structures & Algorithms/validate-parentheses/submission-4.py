class Solution:
    def isValid(self, s: str) -> bool:
        # for every open bracket, add it to the stack
        # for every open parentheses in the stack, 
        # pop the open bracket and move to the next closed bracket
        # the string is valid if the stack if empty 

        stack = []
        closeToOpen = { 
            ")":"(",
            "]":"[", 
            "}":"{"
        }

        for char in s: 
            if char in closeToOpen:
                if not stack: 
                    return False
                if stack[-1] != closeToOpen[char]:
                    return False
                
                stack.pop()
            else: 
                stack.append(char)
        return not stack

























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