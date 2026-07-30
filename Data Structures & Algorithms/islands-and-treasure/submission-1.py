class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        chests = deque()
        visit = set()

        def addCell(r, c):
            if(r<0 or c<0 or r>= ROWS or c>= COLS or grid[r][c]== -1 or (r,c) in visit):
                return
            chests.append((r, c))
            visit.add((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    chests.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while chests:
            for i in range(len(chests)):
                r, c = chests.popleft()
                grid[r][c] = dist
                addCell(r-1, c)
                addCell(r+1, c)
                addCell(r, c-1)
                addCell(r, c+1)
            dist +=1


