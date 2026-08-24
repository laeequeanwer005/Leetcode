class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            len(s)==len(t)
        for i in range(len(s)):
            s[i]==t[i]
            return sorted(s)==sorted(t)
        return True

