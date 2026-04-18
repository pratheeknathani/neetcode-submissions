class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minHeap = []
        for num in count:
            heapq.heappush(minHeap, (count[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        result = []
        for i in range(k):
            freq, num = heapq.heappop(minHeap)
            result.append(num)
        return result