import heapq

def shortestDistance(maze, start, destination):
    # write your code here
    start, destination = tuple(start), tuple(destination)

    def neighbors(maze, node):
        for dir in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            cur_node, dist = list(node), 0
            # print(cur_node, dist)
            # print(len(maze))
            while 0 <= cur_node[0]+dir[0] < len(maze) and \
                  0 <= cur_node[1]+dir[1] < len(maze[0]) and \
                  not maze[cur_node[0]+dir[0]][cur_node[1]+dir[1]]:
                cur_node[0] += dir[0]
                cur_node[1] += dir[1]
                dist += 1
            yield dist, tuple(cur_node)

    heap = [(0, start)]
    visited = set()
    while heap:
        dist, node = heapq.heappop(heap)
        if node in visited: continue
        if node == destination:
            return dist
        visited.add(node)
        # print(visited)
        for neighbor_dist, neighbor in neighbors(maze, node):
            heapq.heappush(heap, (dist+neighbor_dist, neighbor))

    return -1

maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
print(shortestDistance(maze, start, destination))
