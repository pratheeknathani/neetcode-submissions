class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            if two > one:
                heapq.heappush(stones, one-two)
        
        stones.append(0)
        return abs(stones[0])