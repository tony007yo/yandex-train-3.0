from collections import deque
 
def bfs(graph, beg, end):
    max_len = 0
    for vert in graph:
        max_len = max(max_len, len(vert))
    if max_len == 0:
        return -1
    if beg == end:
        return 0
    way = dict()
    way[beg] = 0
    
    queue = deque()
    queue.append((beg, graph[beg]))
    
    founded = False
    
    full_way = dict()
    full_way[beg] = 0
    while queue and not founded:
        beg_v, v_info = queue.popleft()
        for v in v_info:
            if not way.get(v):
                way[v] = way[beg_v] + 1
                full_way[v] = beg_v
                queue.append((v, graph[v]))
            if v == end:
                founded = True
                break
    if founded:
        ready_way = [end]
        next = end
        while len(ready_way) != way[end] + 1:
            next = full_way[next]
            ready_way.append(next)
        ready_way = " ".join(map(str, ready_way[::-1]))
        return f"{way[end]}\n{ready_way}"
    return -1

def gen_adjacency_list(d, V):
    adjacency_list = [[] for _ in range(V)]
    for i in range(1, V):
        vert = list(map(int, d.popleft().split()))
        for j in range(V - 1):
            if vert[j] == 1:
                adjacency_list[i].append(j + 1)

    return adjacency_list

if __name__ == "__main__":
    with open('input.txt', 'r') as f_in:
        d = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    V = int(d.popleft().split()[0])
    V_NEW = V + 1
    
    graph = gen_adjacency_list(d, V_NEW)
    
    begin, end = map(int, d.popleft().split())

    print(bfs(graph, begin, end))