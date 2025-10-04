import heapq

def prim_mst(graph, start=0):
    """
    graph: adjacency list {u: [(v, weight), ...]}
    start: starting vertex
    """
    visited = set()
    min_heap = [(0, start)]  # (weight, vertex)
    mst_weight = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        mst_weight += weight

        if weight != 0:  # Skip the first dummy edge
            mst_edges.append((u, weight))

        for v, w in graph.get(u, []):
            if v not in visited:
                heapq.heappush(min_heap, (w, v))

    return mst_weight, mst_edges


# Example usage
graph = {
    0: [(1, 10), (2, 6)],
    1: [(0, 10), (2, 5), (3, 15)],
    2: [(0, 6), (1, 5), (3, 4)],
    3: [(1, 15), (2, 4)]
}

total_weight, mst = prim_mst(graph)
print("MST weight:", total_weight)
print("Edges in MST:", mst)
