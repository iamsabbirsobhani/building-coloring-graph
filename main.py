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


def check(vertices, upper_limit, vertex_b, graph):
    for i in range(0, upper_limit):
        if vertex_b in graph[vertices[i]]:
            return True
    return False


def welsh_powell_graph_colouring_algorithm(graph, deg_ver):
    # sorted vertices wpgca setp-2
    vertices = []
    # color as number
    colors = 0
    vertices_with_colors = []
    dont_color_vertices = []
    colored_vertices = []
    colored_vertices_per_iter = []

    for i in range(0, len(graph)):
        vertices.append(deg_ver[i][0])

    while len(vertices) > 0:
        for i in range(0, len(vertices)):
            if i > 0 and check(vertices, i, vertices[i], graph):
                dont_color_vertices.append(vertices[i])
            else:
                vertices_with_colors.append((vertices[i], colors))
                colored_vertices.append(vertices[i])
                colored_vertices_per_iter.append((vertices[i], colors))

        print("Vertices: ", vertices)
        print("Colored vertices (v, c): ", colored_vertices_per_iter)

        for i in range(0, len(colored_vertices)):
            vertices.remove(colored_vertices[i])
        colored_vertices = []
        colored_vertices_per_iter = []
        colors += 1
    print("Vertices with colors (v, c): ", vertices_with_colors)
    print("Total color need: ", colors)


# Driver Code
if __name__ == '__main__':
    g = [[] for i in range(5)]
    g = add_edge(g, 0, 1)
    g = add_edge(g, 0, 2)
    g = add_edge(g, 1, 2)
    g = add_edge(g, 1, 3)
    g = add_edge(g, 2, 3)
    g = add_edge(g, 3, 4)
    g = add_edge(g, 3, 0)

    welsh_powell_graph_colouring_algorithm(g, find_degree(g))
