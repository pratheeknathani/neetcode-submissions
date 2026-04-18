class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #ind, temp pairs

        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                oldInd, oldTemp = stack.pop()
                result[oldInd] = ind-oldInd
            stack.append([ind,temp])
        return result