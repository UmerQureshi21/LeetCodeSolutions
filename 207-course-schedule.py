
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}
        
        for pr in prerequisites:
            course = pr[0]
            pre_req = pr[1]
            preMap[course].append(pre_req)
            
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet: # 
                return False
            if preMap[crs] == []: # we are able to take it with no pre req
                return True
            
            visitSet.add(crs)
            
            for pre_req in preMap[crs]:
                result = dfs(pre_req)    
                if not result: 
                    return False
            visitSet.remove(crs)
            preMap[crs] = [] # this course can be reached by other courses, therefore it can be treated as a base case
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
    

preReqs = [[1,0],[2,1],[2,3],[3,2],[5,4],[6,5],[6,3]]

print(Solution().canFinish(len(preReqs), preReqs))