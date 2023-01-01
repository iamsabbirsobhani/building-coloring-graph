def add_edge(adj, v, w):
    adj[v].append(w)
    adj[w].append(v)
    return adj


# degrees of graph, and sort them in descending order
def find_degree(graph):
    deg_vertices = []
    for i in range(0, len(graph)):
        deg_vertices.append((i, len(graph[i])))
    return sorted(deg_vertices, key=lambda deg_ver: deg_ver[1], reverse=True)


def welsh_powell_graph_colouring_algorithm():
    pass


# Driver Code
if __name__ == '__main__':
    g = [[] for i in range(5)]
    print("initial graph: ", g)
    g = add_edge(g, 0, 1)
    g = add_edge(g, 0, 2)
    g = add_edge(g, 1, 2)
    g = add_edge(g, 1, 3)
    g = add_edge(g, 2, 3)
    g = add_edge(g, 3, 4)
    g = add_edge(g, 3, 0)
    print(g)
    print(find_degree(g))
