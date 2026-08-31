class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "]":"[", "}":"{"}
        stack = []
        for l in s:
            if l in closeToOpen:
                if stack and stack[-1] == closeToOpen[l]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        return True if not stack else False

        
