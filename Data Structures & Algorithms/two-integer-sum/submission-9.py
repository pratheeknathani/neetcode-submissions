class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind, val in enumerate(nums):
            search = target - val
            if search in seen:
                return [seen[search], ind]
            seen[val] = ind