class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,1], [0, -1]]
        result = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            area = 1

            while q:
                row, col = q.popleft()
                for x, y in directions:
                    nr, nc = row + x, col + y
                    if (nr<0 or nc<0 or nc>= COLS or nr >= ROWS or grid[nr][nc] == 0):
                        continue
                    area +=1
                    grid[nr][nc] = 0
                    q.append((nr, nc))
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    result = max(result, bfs(r, c))
        
        return result