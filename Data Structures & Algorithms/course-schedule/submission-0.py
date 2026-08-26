class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            
            if preMap[course] == []:
                return True
            
            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            
            visitSet.remove(course)
            preMap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True