# Problem: Find the Minimum Number of Edges to Reverse to Make a Path from Source to Destination
#
# Given a directed graph with n nodes and m edges, determine the minimum number of edges 
# that need to be reversed so that there exists at least one path from a given source node 
# to a given destination node. 
# If it is not possible to form such a path, return -1.
#
# Example 1:
# Input: 
# n = 7
# edges = [(0,1), (2,1), (2,3), (5,1), (4,5), (6,4), (6,3)]
# source = 0, destination = 6
#
# Output: 2
#
# Explanation:
# Reverse the edges (2,1) and (6,3) to create a valid path: 
# 0 → 1 ← 2 → 3 ← 6, so total 2 edges are reversed.
#
# Example 2:
# Input: 
# n = 3
# edges = [(0,1), (2,1)]
# source = 0, destination = 2
#
# Output: 1
#
# Explanation:
# Reverse the edge (2,1) to make the path 0 → 1 → 2.
#
# Example 3:
# Input:
# n = 4
# edges = [(0,1), (2,3)]
# source = 0, destination = 3
#
# Output: -1
#
# Explanation:
# No combination of edge reversals can connect 0 to 3.

# Function to find BFS of Graph from given source s
def bfs(adj):
    
    # get number of vertices
    V = len(adj)
    
    # create an array to store the traversal
    res = []
    s = 0
    # Create a queue for BFS
    from collections import deque
    q = deque()
    
    # Initially mark all the vertices as not visited
    visited = [False] * V
    
    # Mark source node as visited and enqueue it
    visited[s] = True
    q.append(s)
    
    # Iterate over the queue
    while q:
        
        # Dequeue a vertex from queue and store it
        curr = q.popleft()
        res.append(curr)
        
        # Get all adjacent vertices of the dequeued 
        # vertex curr If an adjacent has not been 
        # visited, mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
                
    return res

if __name__ == "__main__":
    
    # create the adjacency list
    # [ [2, 3, 1], [0], [0, 4], [0], [2] ]
    adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
    ans = bfs(adj)
    for i in ans:
        print(i, end=" ")