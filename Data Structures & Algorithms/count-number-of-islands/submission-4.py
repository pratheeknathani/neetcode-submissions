class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        count = 0
        
        def dfs(r, c):
            if (r>= ROWS or r<0 or c>= COLS or c<0 or grid[r][c]=="0"):
                return
            grid[r][c] = "0"
            for x, y in directions:
                newX, newY = x+r, y+c
                dfs(newX, newY)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    dfs(r,c)
                    count +=1
        
        return count

            