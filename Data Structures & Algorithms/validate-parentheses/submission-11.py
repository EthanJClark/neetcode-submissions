class Solution:
    def isValid(self, s: str) -> bool:
        
        closing = {
            '}': "{",
            ']': "[", 
            ')': "(",
            }

        stack = []
        for i in s:
            if i in closing and len(stack) > 0:
                if closing[i] != stack.pop(-1):
                    return False
            else:
                stack.append(i)

        return True if len(stack) == 0 else False