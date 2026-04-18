class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result  = 0
        l = 0
        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l +=1
            result = max(result, prices[r]-prices[l])
        return result