class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #count how many of each
        count = {}
        for val in tasks:
            count[val] = count.get(val, 0) + 1
        maxHeap = []
        for val in count.values():
            heapq.heappush(maxHeap, -val)
        
        q = deque() # [timetobeletgo, remaining]
        time = 0
        while maxHeap or q:
            time +=1 
            if maxHeap:
                val = heapq.heappop(maxHeap) + 1
                if val:
                    q.append((time + n, val))
            else:
                time = q[0][0]
            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q.popleft()[1])
        return time
            
        
