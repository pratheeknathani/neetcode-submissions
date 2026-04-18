class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in my_list:
                return [my_list[complement], i]
            my_list[num] = i
        return []