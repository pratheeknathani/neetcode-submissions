class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        
        leftMax = height[0]
        for i in range(0, len(height)):
            leftMax = max(leftMax, height[i])
            maxL[i] = leftMax

            print(maxL[i])
        

        rightMax = height[-1]
        for i in range(len(height)-1, -1, -1):
            rightMax = max(rightMax, height[i])
            maxR[i] =rightMax

            print(maxR[i])
        
        ans = 0
        for i in range(len(height)):
            ans += min(maxR[i], maxL[i]) - height[i]

        return ans
            