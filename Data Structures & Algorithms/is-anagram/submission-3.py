class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1

        letters2 = {}
        for i in t:
            if i in letters2:
                letters2[i] += 1
            else:
                letters2[i] = 1
        
        for i in letters:
            if i in letters2:
                if letters[i] != letters2[i]:
                    return False
            else:
                return False
        return True
            