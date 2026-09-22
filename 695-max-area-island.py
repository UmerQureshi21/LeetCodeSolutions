from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        if not grid:
            return max_area
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        
        def inBounds(r,c):
            return 0 <= r < rows and 0 <= c < cols
        
        def bfs(r, c):
            q = deque()
            area = 1
            visited.add((r,c))
            q.appendleft((r,c))
            
            while q:
                row, col = q.pop()
                # for each neighbour of (row,col), check if not visited if not then add 
                directions = [(0, -1), (0,1), (-1, 0), (1, 0)]
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    
                    if inBounds(nr,nc) and not (nr,nc) in visited and grid[nr][nc] == 1:
                        visited.add((nr,nc))
                        q.appendleft((nr,nc))
                        area += 1                        
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    if area > max_area:
                        max_area = area
                        
        return max_area
    
    def maxAreaOfIslandDfs(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        
        def dfs(r, c):
            # Base case: out of bounds, water, or already visited
            if (r < 0 or r == ROWS or c < 0 or c == COLS or 
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            # Mark as visited
            visit.add((r, c))
            
            # Return 1 (current cell) + area from all 4 directions
            return (1 + dfs(r + 1, c)    # down
                      + dfs(r - 1, c)    # up
                      + dfs(r, c + 1)    # right
                      + dfs(r, c - 1))   # left
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        
        return area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution().maxAreaOfIslandDfs(grid))
                    