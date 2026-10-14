class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h1 = {}
        h2 = {}

        for i in range(len(s)):
            h1.setdefault(s[i], 0)
            h2.setdefault(t[i], 0)
            h1[s[i]] += 1
            h2[t[i]] += 1

        for i in h1:
            if h1.get(i) != h2.get(i):
                return False

        return True 
