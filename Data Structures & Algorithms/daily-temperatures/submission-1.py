class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #index, temperature pairs

        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                lastInd, lastTemp = stack.pop()
                result[lastInd] = ind-lastInd
            stack.append((ind,temp))
        
        return result