from heapq import heappush, heappop
from math import inf

# A graph implementation using an adjacency matrix.
# All vertices in the graph use integer identifiers.
class Graph:
  def __init__(self):
    self.edges = []


  # Add a vertex to the graph and return its identifier.
  def add_vertex(self):
    if len(self.edges) == 0:
      self.edges = [[None]]
      return 0
    for e in self.edges:
      e.append(None)
    self.edges.append([None] * (len(self.edges) + 1))
    return len(self.edges) - 1

  def _add_edge(self, src, dest, weight):
    self.edges[src][dest] = weight

  def add_edge_directed(self, src, dest, weight):
    self._add_edge(src, dest, weight)

  def add_edge_undirected(self, src, dest, weight):
    self._add_edge(src, dest, weight)
    self._add_edge(dest, src, weight)

  # Returns a list of (vertex, weight) tuples.
  def adjacent(self, src):
    return [(v, weight) for v, weight in enumerate(self.edges[src]) if weight is not None]

  def vertices(self):
    return list(range(len(self.edges)))

class PriorityQueue:
  def __init__(self):
    self.pq = []

  def push(self, item, priority):
    heappush(self.pq, (priority, item))

  def pop(self):
    return heappop(self.pq)

  # Currently runs in O(n) time.
  def prioritize(self, item, priority):
    for i, (it, _) in enumerate(self.pq):
      if it == item:
        del self.pq[i]
    heappush(self.pq, (priority, item))

  def is_empty(self):
    return len(self.pq) == 0

def djikstra(g, src):
  prev, dist = [None] * len(g.vertices()), [None] * len(g.vertices())
  dist[src] = 0
  pq = PriorityQueue()
  for v in g.vertices():
    if v != src:
      dist[v] = inf
    prev[v] = None
    pq.push(v, dist[v])
  while not pq.is_empty():
    _, v = pq.pop()
    for neighbor, weight in g.adjacent(v):
      alt = dist[v] + weight
      if alt < dist[neighbor]:
        dist[neighbor] = alt
        prev[neighbor] = v
        pq.prioritize(v, alt)
  return dist, prev

def main():
  # This graph is the one used in the Wikipedia article on Djikstra's.
  # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#/media/File:Dijkstra_Animation.gif
  g = Graph()
  _ = g.add_vertex()
  v1 = g.add_vertex()
  v2 = g.add_vertex()
  v3 = g.add_vertex()
  v4 = g.add_vertex()
  v5 = g.add_vertex()
  v6 = g.add_vertex()
  g.add_edge_undirected(v1, v2, 7)
  g.add_edge_undirected(v1, v3, 9)
  g.add_edge_undirected(v1, v6, 14)
  g.add_edge_undirected(v2, v3, 10)
  g.add_edge_undirected(v2, v4, 15)
  g.add_edge_undirected(v3, v4, 11)
  g.add_edge_undirected(v3, v6, 2)
  g.add_edge_undirected(v4, v5, 6)
  g.add_edge_undirected(v5, v6, 9)
  src = v1
  dist, prev = djikstra(g, src)
  print('distances from v{} to each vertex:'.format(src))
  for v, d in enumerate(dist):
    print('v{}: {}'.format(v, d))
  print('previous nodes in path, starting from v{}:'.format(src))
  for v, p in enumerate(prev):
    print('prev of v{}: {}'.format(v, p))


if __name__ == '__main__':
  main()
