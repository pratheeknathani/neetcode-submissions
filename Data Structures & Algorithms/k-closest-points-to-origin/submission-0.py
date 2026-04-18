class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = []
        for x,y in points:
            dist = (x**2)+(y**2)
            results.append([dist,x,y])
        
        heapq.heapify(results)
        res = []
        while k > 0:
            dist , x, y = heapq.heappop(results)
            res.append([x,y])
            k -=1
            
        return res