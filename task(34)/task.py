from collections import deque
from threading import stack_size
from sys import setrecursionlimit

setrecursionlimit(1000000)
stack_size(134217728)

def dfs_topsort(graph):
    L = []
    color = { u : 0 for u in graph }
    found_cycle = [False]
    for u in graph:
        if color[u] == 0:
            dfs_visit(graph, u, color, L, found_cycle)
        if found_cycle[0]:
            break
 
    if found_cycle[0]:
        return "-1"

    return " ".join(map(str, L[::-1]))
 
 
def dfs_visit(graph, u, color, L, found_cycle):
    if found_cycle[0]:
        return
    color[u] = 1
    for v in graph[u]:
        if color[v] == 1:
            found_cycle[0] = True
            return
        if color[v] == 0:
            dfs_visit(graph, v, color, L, found_cycle)
    color[u] = 2
    L.append(u)

    
def gen_adjacency_list(d, V, E):
    adjacency_list = dict()
    for i in range(1, V + 1):
        adjacency_list[i] = []
    for _ in range(E):
        v1, v2 = map(int, d.popleft().split())
        adjacency_list[v1].append(v2)
    return adjacency_list

if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        d = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    V, E = map(int, d.popleft().split())
    V_NEW = V + 1

    graph = gen_adjacency_list(d,V,E)

    topology_sort = "-1"
    if V > 1:
        topology_sort = dfs_topsort(graph)
    
    with open('output.txt', 'w') as f_out:
        f_out.writelines(f"{topology_sort}\n")