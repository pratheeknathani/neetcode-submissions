class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]

        total = 0
        for num in nums:
            total += num
            result = max(result, total)
            if total < 0: total = 0
        
        return result