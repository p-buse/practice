import collections

# Find whether there exists a path between two nodes of a graph.
# Using an adjacency matrix.
def bfs(g, src, dest):
    visited = set()
    q = collections.deque([src])
    while q:
        node = q.popleft()
        if node == dest:
            return True
        visited.add(node)
        q.extend(n for n in g.neighbors_of(node) if n not in visited)
    return False

# For an adjaceny list, change q.extend(...) to
# q.extend(n for n in node.neighbors() if n not in visited)
