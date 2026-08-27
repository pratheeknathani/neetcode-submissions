class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while length + num in nums:
                    length +=1 
                result = max(result, length)
        return result