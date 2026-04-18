class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                result = max(length, result)
        return result