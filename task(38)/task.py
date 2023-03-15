from collections import deque

cord_var = [(1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            ]

def gen_neighbors(cord, max_n, max_m, founded):
    i = 1 
    j = 2
    res = []
    for cord_v in cord_var:
        res.append((cord[0] + cord_v[0], cord[1] + cord_v[1]))
    result = set()
    for el in res:
        if (el[0] >= 1 and el[0] <= max_n) and (el[1] >= 1 and el[1] <= max_m) and not el in founded:
            result.add(el)
            founded.add(el)
    return result

def bfs(corm_cord, max_n, max_m, blohi_cords, pole):
    pole[corm_cord[0]][corm_cord[1]] = 0
    queue = deque()
    queue.append((0, corm_cord))
    full_way = 0
    count_of_free_ways = max_n * max_m - 1
    founded = set()
    while count_of_free_ways != 0:
        beg, el = queue.popleft()
        for elem in gen_neighbors(el, max_n, max_m, founded):
            queue.append((beg + 1, elem))

            if pole[elem[0]][elem[1]] == -1:
                pole[elem[0]][elem[1]] = beg + 1
                count_of_free_ways -= 1
        
        if not queue:
            break
        
    full_way = 0
    for bloha_cord in blohi_cords:
        if pole[bloha_cord[0]][bloha_cord[1]] == -1:
            return -1
        full_way += pole[bloha_cord[0]][bloha_cord[1]]
    
    return full_way
    
def get_blohi(Q):
    blohi = list()
    for i in range(Q):
        blohi.append(tuple(map(int, d.popleft().split())))

    return blohi

if __name__ == "__main__":
    with open('input.txt', 'r') as f_in:
        d = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    N, M, S, T, Q = map(int, d.popleft().split())
    blohi = get_blohi(Q)
    pole = [[] for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(M + 1):
            pole[i].append(-1)

    print(bfs((S, T), N, M, blohi, pole))