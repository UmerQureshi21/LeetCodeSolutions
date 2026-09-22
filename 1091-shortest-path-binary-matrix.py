from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        # run bfs on top left if 0, and then check all 8 edges around it as the neightbours
        
        rows = len(grid)
        cols = len(grid[0])
        
        
        if grid[0][0] == 1:
            return -1
        
        visited = set()
        q = deque()
        path_len = 1
        
        visited.add((0,0))
        q.append((0,0,path_len))
        
        def inBounds(r,c):
            return 0 <= r < rows and 0 <= c < cols
        
        while q:
            row, col, path = q.popleft()
            directions = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]
           
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if nr + 1 == rows and nc + 1 == cols and grid[nr][nc] == 0:
                    return path + 1
                elif inBounds(nr,nc) and not (nr,nc) in visited and grid[nr][nc] == 0:
                    visited.add((nr,nc))
                    q.append((nr, nc, path + 1))
                
        return - 1
    
grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[0,1],[1,0]]

print(Solution().shortestPathBinaryMatrix(grid))