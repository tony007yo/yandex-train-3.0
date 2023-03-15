from collections import deque

def bfs(lines, M, A, B):   
    current = deque()
    founded = set()
    current.append(([A], 0))
    founded.add(A)
    
    while current:
        verts, prev_step = current.popleft()

        for vert in verts:
            for el in lines[vert]:
                if el not in founded:
                    current.append((lines[vert], prev_step + 1))
                    founded.add(el)

        if B in founded:
            return str(prev_step)


    return str(-1)
    
def get_lines(N, M, d):
    lines = [set() for _ in range(N + 1)]
    for i in range(M):
        line = list(map(int, d.popleft().split()[1::]))
        while line:
            vert = line.pop()
            for l in line:
                lines[vert].add(l)
                lines[l].add(vert)

    return lines

if __name__ == "__main__":
    with open('input.txt', 'r') as f_in:
        d = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    N = int(d.popleft().split()[0])
    M = int(d.popleft().split()[0])
    lines = get_lines(N, M, d)
    A, B = map(int, d.popleft().split())
    
    with open('output.txt', 'w') as f_out:   
        f_out.write( bfs(lines, M, A, B))