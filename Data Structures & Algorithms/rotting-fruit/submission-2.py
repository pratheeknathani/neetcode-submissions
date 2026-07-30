class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        q = deque()
        fresh = 0

        def rot(r, c):
            if (r<0 or c<0 or r>= ROWS or c>= COLS or grid[r][c] != 1 or (r,c) in seen):
                return
            q.append((r,c))
            seen.add((r,c))
            nonlocal fresh
            fresh -=1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    seen.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = 2
                rot(row-1, col)
                rot(row+1, col)
                rot(row, col-1)
                rot(row, col+1)
            time +=1
        
        return time if fresh == 0 else -1
    