class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rot = deque()
        seen = set()
        count = 0

        #find the initial rotten and count how many fresh
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rot.append((r,c))
                elif grid[r][c]== 1:
                    count +=1
        
        #rot the fruit
        def rotFruit(r, c):
            if r<0 or c<0 or r>= ROWS or c>=COLS or (r,c) in seen or grid[r][c]!= 1:
                return
            nonlocal count
            count -= 1
            grid[r][c]=2
            rot.append((r,c))
            seen.add((r,c))
        
        time = 0
        while rot and count>0:
            for _ in range(len(rot)):
                r, c = rot.popleft()
                rotFruit(r-1,c)
                rotFruit(r+1,c)
                rotFruit(r,c-1)
                rotFruit(r,c+1)
            time += 1
        
        return time if count == 0 else -1