class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {"[": "]","(": ")", "{": "}" }
        stack = []
        if(len(s) %2 == 1):
            return False
        for i in range(len(s)):
            if(s[i] not in my_dict):
                if(len(stack)> 0 and my_dict[stack[-1]] == s[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        return len(stack) == 0
