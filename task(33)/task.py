from collections import deque

res = "YES"
def DFS(vertex, graph, color_end, color_l, coloring):
    global res
    color_l[vertex] = 1
    for u in graph[vertex]:
        if color_l[u] == 0:
            color = coloring[vertex] + 1
            coloring[u] = color % 2
            DFS(u, graph, color_end, color_l, coloring)
        else:
            if coloring[vertex] == coloring[u] and res != "NO":
                res = "NO"

    color_l[vertex] = 2
    color_end = coloring[vertex]


def gen_adjacency_list(d, V, E):
    adjacency_list = [[] for _ in range(V)]
    for _ in range(E):
        v1, v2 = map(int, d.popleft().split())
        adjacency_list[v1].append(v2)
        adjacency_list[v2].append(v1)
    return adjacency_list


if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        d = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    V, E = map(int, d.popleft().split())
    V_NEW = V + 1
    
    graph = gen_adjacency_list(d, V_NEW, E)
    
    color = [0 for _ in range(V_NEW)]
    coloring = [0 for _ in range(V_NEW)]
    color_end = 0

    for i in range(1, V_NEW):
        if (color[i] == 0):
            coloring[i] = (color_end + 1) % 2
            DFS(i, graph, color_end, color, coloring)

    print(res)