class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for val in s:
            if val in closeToOpen:
                if stack and stack[-1] == closeToOpen[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        
        return len(stack) == 0
                