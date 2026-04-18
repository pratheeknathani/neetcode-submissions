class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        for i in range (len(heights)):
            r = len(heights) -1
            while i<r:
                temp = ((r-i) * min(heights[i], heights[r]))
                if temp > biggest:
                    biggest = temp
                r-=1
        return biggest