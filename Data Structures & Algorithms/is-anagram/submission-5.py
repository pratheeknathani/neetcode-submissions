class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        validS = [0] * 26
        validT = [0] * 26
        for i in range(len(s)):
            validS[ord('a')-ord(s[i])] +=1
            validT[ord('a')-ord(t[i])] += 1
        
        return validS == validT