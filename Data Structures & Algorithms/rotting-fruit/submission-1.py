class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        seen = set()
        count = 0

        #add rotten fruit to quuee
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    seen.add((r,c))
                if grid[r][c] == 1:
                    count +=1
        
        def addVal(r,c):
            if(r<0 or c<0 or r==ROWS or c==COLS or (r,c) in seen or grid[r][c] != 1):
                return
            q.append((r,c))
            seen.add((r,c))
            nonlocal count
            count -=1

        time = 0
        while q and count>0:
            for i in range(len(q)):
                r, c = q.popleft()
                addVal(r-1, c)
                addVal(r+1, c)
                addVal(r, c-1)
                addVal(r, c+1)
            time +=1
        return time if count == 0 else -1


