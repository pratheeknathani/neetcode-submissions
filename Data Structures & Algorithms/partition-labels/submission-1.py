class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, v in enumerate(s):
            lastIndex[v] = i
        
        result = []
        end = size = 0
        for i, c in enumerate(s):
            size +=1
            end = max(end, lastIndex[c])

            if i == end:
                result.append(size)
                size = 0
        
        return result