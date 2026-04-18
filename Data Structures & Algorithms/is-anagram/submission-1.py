class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        stringS = [0] *26
        stringT = [0]*26
        for i in range(len(s)):
            stringS[ord(s[i])-ord("a")] += 1
            stringT[ord(t[i])-ord("a")] += 1
        return stringS == stringT