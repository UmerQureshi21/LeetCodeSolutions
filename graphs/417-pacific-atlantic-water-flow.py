from collections import deque

class Solution:
    def pacificAtlanticBruteForce(self, heights: list[list[int]]) -> list[list[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        result = []
        
        def reachPacific(r,c):
            return r == 0 or c == 0
        def reachAtlantic(r,c):
            return r == rows - 1 or c == cols - 1
        def inBounds(r,c):
            return 0 <= r < rows and 0 <= c < cols
        
        
        def bfs(row,col):
            q = deque([(row,col)])
            visited = set([(row,col)])
            directions = [(0,-1), (0, 1), (-1, 0), (1,0)]
            reach_atlantic = reachPacific(row,col)
            reach_pacific = reachAtlantic(row,col)
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    coord = (nr,nc)
                    if inBounds(nr,nc) and heights[nr][nc] <= heights[r][c] and not coord in visited:
                        q.append(coord)
                        visited.add(coord)
                        reach_atlantic = reachAtlantic(nr,nc)
                        reach_pacific = reachPacific(nr,nc)
            
            return reach_pacific and reach_atlantic
                        
        for row in range(rows):
            for col in range(cols):
                if bfs(row,col):
                    result.append([row,col])
                    
        return result
    
    def attempt(self, heights: list[list[int]]) -> list[list[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        results = []
        
        def inBounds(r,c):
            return 0 <= row and row < rows and 0<= col and col < cols
        
        #visit all reachable cells from pacific ocean
        p_visited = set()
        a_visited = set()
        
        def p_bfs(row,col):
            q = deque([(row,col)])
            p_visited.add((row,col))
            directions = [(0,-1), (0, 1), (-1, 0), (1, 0)]
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    n_coord = (nr,nc)
                    if heights[nr][nc] >= heights[r][c] and not n_coord in p_visited:
                        p_visited.add(n_coord)
                        q.append(n_coord)
        
        def a_bfs(row,col):
            q = deque([(row,col)])
            a_visited.add((row,col))
            directions = [(0,-1), (0, 1), (-1, 0), (1, 0)]
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    n_coord = (nr,nc)
                    if heights[nr][nc] >= heights[r][c] and not n_coord in a_visited:
                        a_visited.add(n_coord)
                        q.append(n_coord)
                        if n_coord in p_visited:
                            results.append(n_coord)
                    
        
        #do a bfs 0th row
        for col in range(rows):
            p_bfs(0,col)
        for row in range(cols):
            p_bfs(row,0)
        for col in range(rows):
            p_bfs(rows - 1,col)
        for row in range(cols):
            p_bfs(row,cols - 1)
        return results
    
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        results = []
        
        def inBounds(r,c):
            return 0 <= r and r < ROWS and 0<= c and c < COLS
        
        def dfs(r,c,visit,prev_height):
            if (r,c) in visit or not inBounds(r,c) or heights[r][c] < prev_height:
                return
            visit.add((r,c))
            
            for dr, dc in [(0,-1), (0,1), (1,0), (-1,0)]:
                dfs(r + dr, c + dc, visit, heights[r][c])
            
            
        # first row is pacici
        for c in range(COLS):
            dfs(0,c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
            
        #last row is atlantic
        for r in range(ROWS):
            dfs(0,r, pac, heights[0][r])
            dfs(COLS - 1, r, atl, heights[COLS - 1][r])            
        
        for r in range(ROWS):
            for c in range(COLS):
                if heights[r][c] in pac and heights[r][c]:
                    results.append([r,c])
        return results