from collections import deque

def iterativeDFS(graph, discovered, v):
    stack = deque()
    stack.append(v)
    res = []
    while stack:
        v = stack.pop()
 
        if discovered[v]:
            continue
        discovered[v] = True
        res.append(v)
        
        adjList = graph[v][::-1]
        for i in range(len(adjList)):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)
    
    return sorted(res)


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
    
    visited = [False for _ in range(V_NEW)]
    adjacency_list = gen_adjacency_list(d, V_NEW, E)
    
    res = iterativeDFS(adjacency_list, visited, 1)
    
    len_res = len(res)
    res = " ".join(map(str, res))

    with open('output.txt', 'w') as f_out:
        f_out.writelines(f"{len_res}\n{res}")
    