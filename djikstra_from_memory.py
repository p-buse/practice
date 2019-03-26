def djikstras(g, src):
    for v in g.vertices:
        if v == src:
            dist[v] = 0
        else:
            dist[v] = inf
        prev[v] = None
        pq.push(dist[v], v)

    while not pq.is_empty():
        v = pq.pop()
        for w, n in g.adjacent(v):
            alt = dist[v] + w
            if alt < dist[n]:
                dist[n] = alt
                prev[n] = v
                pq.reprioritize(dist[n], n)
    return dist, prev
