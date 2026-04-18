class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for ind, num in enumerate(nums):
            search = target - num
            if search in map:
                return [map[search], ind]
            else:
                map[num] = ind