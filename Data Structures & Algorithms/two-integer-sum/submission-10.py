class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind, num in enumerate(nums):
            search = target - num
            if search in seen:
                return [seen[search], ind]
            else:
                seen[num] = ind