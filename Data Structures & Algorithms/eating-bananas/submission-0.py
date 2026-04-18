import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r

        while l<=r:
            mid = (r+l) // 2
            temp = 0
            for i in piles:
                temp += math.ceil(float(i)/mid)
            if temp<=h:
                r = mid-1
                result = mid
            else:
                l = mid+1
        return result