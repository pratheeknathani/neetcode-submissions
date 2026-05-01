class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indMap = {}
        for i, x in enumerate(nums):
            search = target - x
            if search in indMap:
                return[indMap[search], i]
            else:
                indMap[x] = i
        