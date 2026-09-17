class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False

        stack = []

        key = {
            '}' : '{',
            ']' : '[' ,
            ')' : '(' ,
        }

        for i in s:
            if i in [']','}',')'] and len(stack) > 0:
                if stack[-1] != key[i] :
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(i)
        
        return False if len(stack) > 0 else True

            


