class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal_mst(vertices, edges):
    """
    vertices: number of vertices (0 to V-1)
    edges: list of tuples (weight, u, v)
    """
    edges.sort()  # Sort edges by weight
    ds = DisjointSet(vertices)
    mst_weight = 0
    mst_edges = []

    for weight, u, v in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_weight += weight
            mst_edges.append((u, v, weight))

    return mst_weight, mst_edges


# Example usage
V = 4
edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 1, 2),
    (15, 1, 3),
    (4, 2, 3)
]

total_weight, mst = kruskal_mst(V, edges)
print("MST weight:", total_weight)
print("Edges in MST:", mst)
