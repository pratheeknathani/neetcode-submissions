class Solution:
    def isValid(self, s: str) -> bool:
        validSet = {"[": "]","(": ")", "{": "}" }
        stack = []

        for char in s:
            if char not in validSet:
                if stack and validSet[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
            