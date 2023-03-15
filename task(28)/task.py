from collections import deque

def calculate(count_of_lines, count_of_els):
    res = [[] for _ in range(count_of_lines)]
    for i in range(count_of_lines):
        for _ in range(count_of_els):
            res[i].append(0)
    res[0][0] = 1
    for i in range(1, count_of_lines):
        for j in range(1, count_of_els):
            if i - 2 >= 0 and j - 1 >= 0:
                res[i][j] += res[i - 2][j - 1]
            if i - 1 >= 0 and j - 2 >= 0:
                res[i][j] += res[i - 1][j - 2]

    return f"{res[-1][-1]}"

if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        data = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    N, M = map(int, data.popleft().split())
    print(calculate(N, M))
