class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = []
        for i in range(len(position)):
            result.append((position[i], speed[i]))
        result.sort(reverse = True)

        stack = []

        for p, s in result:
            stack.append((target-p)/s)
            if (len(stack)>=2 and stack[-1]<=stack[-2]):
                stack.pop()
        
        return len(stack)
            
        
