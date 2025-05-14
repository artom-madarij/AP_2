def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    farms = lines[0].split(',')
    stores = lines[1].split(',')
    roads = []
    for line in lines[2:]:
        a, b, c = line.split(',')
        roads.append((a, b, int(c)))
    return farms, stores, roads

def build_graph(farms, stores, roads):
    graph = {}

    def add_edge(u, v, capacity):
        if u not in graph:
            graph[u] = {}
        if v not in graph[u]:
            graph[u][v] = 0
        graph[u][v] += capacity

        if v not in graph:
            graph[v] = {}
        if u not in graph[v]:
            graph[v][u] = 0

    for u, v, c in roads:
        add_edge(u, v, c)

    for farm in farms:
        add_edge('main_source', farm, float('inf'))
    for store in stores:
        add_edge(store, 'main_sink', float('inf'))

    return graph

def bfs(residual_graph, source, sink, parent):
    visited = set()
    queue = [source]
    parent.clear()
    parent[source] = None

    while queue:
        u = queue.pop(0)
        for v, capacity in residual_graph.get(u, {}).items():
            if v not in visited and capacity > 0:
                parent[v] = u
                if v == sink:
                    return True
                visited.add(v)
                queue.append(v)
    return False

def ford_fulkerson(graph, source, sink):
    parent = {}
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

def main():
    farms, stores, roads = read_file('input.txt')
    graph = build_graph(farms, stores, roads)
    max_delivery = ford_fulkerson(graph, 'main_source', 'main_sink')
    print(max_delivery)

if __name__ == '__main__':
    main()
