class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = {}
        for index, num in enumerate(numbers):
            check = target - num
            if check in count:
                return [count[check]+1, index+1]
            count[num] = index