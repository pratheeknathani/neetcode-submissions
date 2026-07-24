from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, cols = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        islands = 0

        def bfs(r, c):
            grid[r][c] = "0"
            q = deque()
            q.append((r,c))
            while q:
                nr, nc = q.popleft()
                for x, y in directions:
                    nx, ny = nr + x, nc + y
                    if (nx<0 or ny <0 or nx>= row or ny >= cols or grid[nx][ny] == "0"):
                        continue
                    grid[nx][ny] = "0"
                    q.append((nx,ny))
                
        
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands           
