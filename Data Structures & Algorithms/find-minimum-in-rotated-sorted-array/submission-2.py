class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) -1
        min_nums = nums[l]
        while l<=r:
            middle = l+((r-l)//2)
            if nums[middle]>nums[r]:
                l = middle + 1
            elif nums[middle]<=nums[l] and nums[middle]<min_nums:
                min_nums = nums[middle]
            else:
                r = middle -1
        return min_nums
                