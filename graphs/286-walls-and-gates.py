from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]):
        ROWS = len(rooms)
        COLS = len(rooms[0])
        INF = 2147483647
        q = deque()
        
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    q.append((row,col,0))
        visited = {}
        def inBounds(r,c):
            return 0 <= r and r < ROWS and 0 <= c and c < COLS        
        # only called on 0 cells, only visiitng INF neighbours
        def bfs():            
            while q:
                r,c, distance = q.popleft()
                for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if inBounds(nr,nc) and rooms[nr][nc] == INF and not (nr,nc) in visited:
                        q.append((nr,nc,distance + 1))
                        visited[(nr,nc)] = distance + 1        
        bfs()
        for coord in visited:
            if not visited[coord] == 0:
                rooms[coord[0]][coord[1]] = visited[coord]
        return rooms    
        

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

print(Solution().islandsAndTreasure(rooms))