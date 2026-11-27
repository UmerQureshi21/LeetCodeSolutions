from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        minute = 0
        
        q = deque()
        visited = set()
        
        one_count = 0
        
        def inBounds(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    one_count += 1
                elif grid[row][col] == 2:
                    q.append((row, col, minute))
                    visited.add((row, col))
                    
        while one_count >= 0 and q:
            row, col, curr_minute = q.popleft()
            print(f"curr_minute: {curr_minute}\none_count: {one_count}")
            directions = [(0,-1), (0,1), (-1, 0), (1, 0)]
            
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                new_coord =(nr,nc)
                
                if inBounds(nr, nc) and grid[nr][nc] == 1 and not new_coord in visited:
                    grid[nr][nc] = 2
                    one_count -= 1
                    visited.add(new_coord)
                    q.append((nr,nc,curr_minute + 1))
            minute = curr_minute
            
        
        if one_count > 0:
            return -1       
        return minute



grid = [[2,1,1],[1,1,0],[0,1,1]]
#grid = [[2,1,0,0,1],[1,1,1,1,2],[0,0,1,1,1],[1,2,1,0,1]]

print(Solution().orangesRotting(grid))
            
        