from math import inf


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def insert(self, item, priority):
        self.items.append((priority, item))
        self.items = sorted(self.items)

    def pop(self):
        item = self.items[0][1]
        del self.items[0]
        return item

    def set_priority(self, item, priority):
        index = -1
        for i in range(len(self.items)):
            if item == self.items[i][1]:
                index = i
        (_, item) = self.items[index]
        del self.items[index]
        self.items.append((priority, item))
        self.items = sorted(self.items)

class Graph:
    def __init__(self):
        self.edges = []
    
    def add_vertex(self):
        """Add a vertex to the graph and return its index."""
        if not self.edges:
            self.edges = [[0]]
            return 0
        self.edges.append([0]*len(self.edges[0]))
        for e in self.edges:
            e.append(0)
        return len(self.edges) - 1

    def _add_edge(self, src, dest, weight):
        self.edges[src][dest] = weight
    
    def add_edge_directed(self, src, dest, weight):
        self._add_edge(src, dest, weight)

    def add_edge_undirected(self, src, dest, weight):
        self._add_edge(src, dest, weight)
        self._add_edge(dest, src, weight)

    @property
    def vertices(self):
        return list(range(len(self.edges)))

    def edge(self, src, dest):
        return self.edges[src][dest]

    def neighbors(self, v):
        """Returns a list of tuples of (neighbor, weight) pairs."""
        return list(enumerate(self.edges[v]))

def djikstra(g, src):
    pq = PriorityQueue()
    dist, prev = [0] * len(g.vertices), [0] * len(g.vertices)
    dist[src] = 0
    for v in g.vertices:
        if v != src:
            dist[v] = inf
        prev[v] = None
        pq.insert(v, 0)
    u = pq.pop()
    while not pq.is_empty():
        for v, weight in g.neighbors(u):
            if weight == 0:
                continue
            tentative = dist[u] + weight
            if tentative < dist[v]:
                dist[v] = tentative
                prev[v] = u
                pq.set_priority(v, tentative)
        u = pq.pop()
    return dist, prev

def main():
    g = Graph()
    v0 = g.add_vertex()
    v1 = g.add_vertex()
    v2 = g.add_vertex()
    v3 = g.add_vertex()
    v4 = g.add_vertex()
    v5 = g.add_vertex()
    v6 = g.add_vertex()
    g.add_edge_undirected(v1, v2, 7)
    g.add_edge_undirected(v1, v6, 14)
    g.add_edge_undirected(v1, v3, 9)
    g.add_edge_undirected(v2, v3, 10)
    g.add_edge_undirected(v2, v4, 15)
    g.add_edge_undirected(v3, v6, 2)
    g.add_edge_undirected(v3, v4, 11)
    g.add_edge_undirected(v4, v5, 6)
    g.add_edge_undirected(v5, v6, 9)
    dist, prev = djikstra(g, v1)
    print('dist: {}'.format(list(enumerate(dist))))
    print('prev: {}'.format(list(enumerate(prev))))

if __name__ == '__main__':
    main()