class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minHeap = []
        for val in count:
            heapq.heappush(minHeap, (count[val], val))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        result = []
        for i in range(k):
            freq, val = heapq.heappop(minHeap)
            result.append(val)
        
        return result