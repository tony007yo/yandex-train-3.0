from collections import deque

def gen_neighbors(cord, max_n, founded):
    cords_var = [(0,0,1), (0,1,0), (1,0,0), (0,0,-1), (0,-1,0), (-1,0,0)]
    res = []
    for i, j, k in cords_var:
        res.append((cord[0] + i, cord[1] + j, cord[2] + k))
    result = set()
    for el in res:
        if not el in founded and (el[0] >= 0 and el[0] < max_n) and (el[1] >= 0 and el[1] < max_n) and (el[2] >= 0 and el[2] < max_n):
            result.add(el)
            founded.add(el)
    return result

def bfs(speleolog_cord, max_n, pole):
    queue = deque()
    queue.append((0, speleolog_cord))
    full_way = 0
    founded = set()
    found = False
    end_coord = 0
    while queue and not found:
        beg, el = queue.popleft()
        for elem in gen_neighbors(el, max_n, founded):
            if pole[elem[0]][elem[1]][elem[2]] == -2:
                continue
            queue.append((beg + 1, elem))

            if pole[elem[0]][elem[1]][elem[2]] == -1:
                pole[elem[0]][elem[1]][elem[2]] = beg + 1
                if elem[0] == 0:
                    found = True
                    end_coord = (elem[0], elem[1], elem[2])
                    break
        
    full_way = pole[end_coord[0]][end_coord[1]][end_coord[2]]
    
    return full_way
    
def get_cube(N, d):
    cube = [ [ [ -2 for _ in range(N)] for _ in range(N)] for _ in range(N)]
    speleolog_cord = None
    end_coords = []
    for i in range(N):
        for j in range(N):
            line = d.popleft()
            if line == '':
                line = d.popleft()
            for k in range(N):
                if line[k] == ".":
                    cube[i][j][k] = -1
                    if i == 0:
                        end_coords.append((i, j ,k))
                elif line[k] == "S":
                    cube[i][j][k] = 0
                    speleolog_cord = (i, j, k)

    return speleolog_cord, end_coords, cube

if __name__ == "__main__":
    with open('input.txt', 'r') as f_in:
        d = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    N = int(d.popleft().split()[0])
    speleolog_cord, end_coords, cube = get_cube(N, d)
    
    print(bfs(speleolog_cord, N, cube))