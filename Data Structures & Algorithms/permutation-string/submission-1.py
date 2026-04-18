class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        

        s1t = [0] * 26
        s2t = [0] * 26
        matches = 0
        for i in range(len(s1)):
            s1t[ord(s1[i]) - 97] += 1
        for i in range(len(s1)):
            s2t[ord(s2[i]) - 97] += 1
        
        for i in range(26):
            if s1t[i] == s2t[i]:
                matches+=1
        
        if matches == 26:
            return True

        for i in range(1, len(s2)-len(s1)+1):
            if (s1t[ord(s2[i-1]) - 97]) == s2t[(ord(s2[i-1]) - 97)]:
                matches -=1
            s2t[ord(s2[i-1]) - 97] -=1
            if s2t[ord(s2[i-1])-97] == s1t[ord(s2[i-1])-97]:
                matches +=1

            if (s1t[ord(s2[i+len(s1)-1]) - 97]) == s2t[(ord(s2[i+len(s1)-1]) - 97)]:
                matches -=1
            s2t[ord(s2[i+len(s1)-1]) - 97] +=1
            if s2t[ord(s2[i+len(s1)-1])-97] == s1t[ord(s2[i+len(s1)-1])-97]:
                matches +=1
            if matches==26:
                return True

        
        return False

        


        

        