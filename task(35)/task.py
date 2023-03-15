from collections import deque
 
def dfs_cycle(vert, p, color: list,
              par: list):
 
    if color[vert] == 2:
        return
 
    if color[vert] == 1:
        v = []
        cur = p
        v.append(cur)
 
        while cur != vert:
            cur = par[cur]
            v.append(cur)
        cycles.append(v)
 
        return
    if p:
        par[vert] = p
 
    color[vert] = 1
 
    for v in graph[vert]:
 
        if v == par[vert]:
            continue
        dfs_cycle(v, vert, color, par)
 
    color[vert] = 2
  
def gen_adjacency_list(d, V):
    adjacency_list = list()
    for i in range(1, V):
        vert = list(map(int, d.popleft().split()))
        for j in range(V - 1):
            if vert[j] == 1:
                adjacency_list.append((i, j + 1))

    return adjacency_list

if __name__ == "__main__":
    with open('input.txt', 'r') as f_in:
        d = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    V = int(d.popleft().split()[0])
    V_NEW = V + 1
    
    graph = [[] for _ in range(V_NEW)]
    cycles = []

    adjacency_list = gen_adjacency_list(d, V_NEW)
    for el in adjacency_list:
        graph[el[0]].append(el[1])
    
    res = ["NO"]
    
    color = [0] * V_NEW
    parent = [0] * V_NEW
    
    for i in range(1, V_NEW):
        dfs_cycle(i, None, color, parent)
        if len(cycles) > 0:
            res = ["YES"]
            res.append(str(len(cycles[0])))
            line = " ".join(map(str, cycles[0]))
            res.append(line)
            break

    with open('output.txt', 'w') as f_out:
        f_out.writelines("\n".join(res))