from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        starting_colour = image[sr][sc]
        
        # Edge case: if already the target color, no changes needed
        if starting_colour == color:
            return image
        
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        image[sr][sc] = color
        rows = len(image)
        cols = len(image[0])
        
        while q:
            row, col = q.popleft()  # Use popleft() for BFS bc its q
            
            # Check all 4 neighbors
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nr, nc = row + dr, col + dc
                
                # Only add if: in bounds, not visited, AND matches original color
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and image[nr][nc] == starting_colour:
                    visited.add((nr, nc))
                    image[nr][nc] = color
                    q.append((nr, nc))
        
        return image
    
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
    
print(Solution().floodFill(image,sr,sc,color))
