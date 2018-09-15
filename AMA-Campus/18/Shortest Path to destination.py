class Solution:
    """
    @param targetMap: 
    @return: nothing
    """
    def shortestPath(self, targetMap):
        # Write your code here
        if not targetMap:
            return 
        
        return self.bfs(targetMap, 0, 0)
        
    def bfs(self, targetMap, x, y):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        targetMap[x][y] = 1
        queue = collections.deque([[x, y]])
        step = -1
        
        while queue:
            length = len(queue)
            step += 1
            
            for _ in range(length):
                cur = queue.popleft()
                # check cur 
                if targetMap[cur[0]][cur[1]] == 2:
                    return step
                
                # add valid neighbors
                for direction in directions:
                    neighborX = cur[0] + direction[0]
                    neighborY = cur[1] + direction[1]
                    if self.nonObstacle(targetMap, neighborX, neighborY):
                        # mark as visited
                        targetMap[cur[0]][cur[1]] = 1
                        queue.append([neighborX, neighborY])
                
        return -1 
        
    def nonObstacle(self, targetMap, x, y):
        m = len(targetMap)
        n = len(targetMap[0])
        return 0 <= x < m and 0 <= y < n and targetMap[x][y] != 1
