class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        for val in count.values():
            heapq.heappush(maxHeap, -val)
        
        q = deque() #[count, validTime]
        time = 0
        while maxHeap or q:
            time +=1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time