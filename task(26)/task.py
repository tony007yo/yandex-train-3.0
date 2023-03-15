from collections import deque

def calculate(data, count_of_lines, count_of_els):
    line = tuple(map(int, data.popleft().split()))
    res = [[] for _ in range(count_of_lines)]
    res[0].append(line[0])
    for i in range(1, count_of_els):
        res[0].append(line[i] + res[0][i - 1])
    j = 1
    while len(data) > 0:
        line = tuple(map(int, data.popleft().split()))
        res[j].append(line[0] + res[j - 1][0])
        for i in range(1, count_of_els):
            res[j].append(min(res[j][i - 1], res[j - 1][i]) + line[i])
        j += 1
    return str(res[-1][-1])

if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        data = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    N, M = map(int, data.popleft().split())
    print(calculate(data, N, M))