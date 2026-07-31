class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        chests = deque()
        seen = set()

        def addCell(r,c):
            if (r<0 or r>= ROWS or c<0 or c>= COLS or (r,c) in seen or grid[r][c]== -1):
                return
            chests.append((r,c))
            seen.add((r,c))

        #finding the chests
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    chests.append((r,c))
                    seen.add((r,c))
        
        #run bfs from chests

        dist = 0
        while chests:
            for i in range(len(chests)):
                row, col = chests.popleft()
                grid[row][col] = dist
                addCell(row-1, col)
                addCell(row+1, col)
                addCell(row, col-1)
                addCell(row, col+1)
            dist +=1
