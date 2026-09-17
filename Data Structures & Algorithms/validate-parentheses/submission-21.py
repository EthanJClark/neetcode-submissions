class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        key = {
            '}' : '{',
            ']' : '[' ,
            ')' : '(' ,
        }

        for i in s:
            if i in key and len(stack) > 0:
                if stack[-1] != key[i] :
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(i)
        
        return False if len(stack) > 0 else True

            


