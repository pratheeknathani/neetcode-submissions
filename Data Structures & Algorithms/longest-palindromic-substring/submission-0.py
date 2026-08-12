class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0
        for i in range(len(s)):
            #odd case aba
            l, r = i, i
            while l >= 0 and r<len(s) and s[r] == s[l]:
                if (r-l+1 > resLen):
                    result = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            
            l, r = i, i+1
            while l >= 0 and r<len(s) and s[r] == s[l]:
                if (r-l+1 > resLen):
                    result = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return result
