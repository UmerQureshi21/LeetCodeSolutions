from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        
        queue = deque()
        visited = set() #set of (row,col)
        
        for row in range(rows):
            for col in range(cols):
                coords = (row,col)
                if not coords in visited and grid[row][col] == "1": # do bfs on this
                    queue.appendleft(coords)
                    visited.add(coords)
                    while len(queue) > 0:
                        curr = queue.pop()
                        currR = curr[0]
                        currC = curr[1]
                        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                            nr, nc = currR + dr, currC + dc

                            if 0 <= nr < rows and 0 <= nc < cols and not (nr,nc) in visited and grid[nr][nc] == "1":
                                visited.add((nr,nc))
                                queue.appendleft((nr,nc))
                    island_count += 1
        
        
                    
            
            
            
            
        return island_count
    
    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    
print(Solution().numIslands(grid))