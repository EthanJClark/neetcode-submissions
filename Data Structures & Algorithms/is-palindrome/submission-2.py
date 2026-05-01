class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([(x.lower() if x.isalpha() or x.isdecimal() else "") for x in s])

        length = len(s)
        
        for i in range(length):
            if s[i] != s[length-i-1]:
                return False

        return True