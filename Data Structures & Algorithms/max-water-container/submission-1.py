class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        biggest = 0
        for i in range (len(heights)):
            while l<r:
                temp = ((r-l) * min(heights[l], heights[r]))
                if temp > biggest:
                    biggest = temp
                if heights[l] < heights[r]:
                    l +=1
                else:
                    r-=1
        return biggest