from collections import deque

def iterativeDFS(graph, discovered, n):
    answer = 0
    for i in range(n):
        if discovered[i]:
            continue

        answer += 1
        discovered[i] = i
        queue = [i]
        while queue:
            v = queue.pop()
            for to in graph[v]:
                if not discovered[to]:
                    discovered[to] = i
                    queue.append(to)
        
    comp = dict()
    for i in range(1, n):
        if not comp.get(discovered[i]):
            comp[discovered[i]] = []
        comp[discovered[i]].append(str(i))

    return comp

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
    
    adjacency_list = gen_adjacency_list(d, V_NEW, E)
    res = set()
    
    visited = [False for _ in range(V_NEW)]
    components = iterativeDFS(adjacency_list, visited, V_NEW)
    len_res = len(components)
    
    out_dict = dict()
    for value in components.values():
        if not out_dict.get(len(value)):
            out_dict[len(value)] = []
        out_dict[len(value)].append(value)

    with open('output.txt', 'w') as f_out:
        f_out.writelines(f"{len_res}\n")
        for i in range(V_NEW, 0, -1):
            comp = out_dict.get(i)
            if comp:
                for el in comp:
                    l = " ".join(el) 
                    f_out.writelines(f"{len(el)}\n{l}\n")