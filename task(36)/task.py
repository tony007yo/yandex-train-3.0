from collections import deque
 
def bfs(graph, beg, end):
    way = [-1] * len(graph)
    queue = deque()
    queue.append((beg, graph[beg]))
    way[beg] = 0

    founded = False
    while queue and not founded:
        beg_v, v_info = queue.popleft()
        for v in v_info:
            if way[v] == -1:
                way[v] = way[beg_v] + 1
                queue.append((v, graph[v]))
            if v == end:
                founded = True
                break
    return way[end] if founded else -1

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