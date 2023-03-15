from collections import deque

def calculate(data, count_of_lines, count_of_els):
    line = tuple(map(int, data.popleft().split()))
    res = [[] for _ in range(count_of_lines)]
    res[0].append((line[0], "R"))
    for i in range(1, count_of_els):
        res[0].append((line[i] + res[0][i - 1][0], "R"))
    j = 1
    maxim = None
    while len(data) > 0:
        line = tuple(map(int, data.popleft().split()))
        res[j].append((line[0] + res[j - 1][0][0], "D"))
        for i in range(1, count_of_els):
            if res[j][i - 1][0] > res[j - 1][i][0]:
                maxim = (res[j][i - 1][0] + line[i], "R")
            else:
                maxim = (res[j - 1][i][0] + line[i], "D")
            res[j].append(maxim)
        j += 1
    i, j = count_of_els - 1, count_of_lines - 1
    result_way = []
    while not(i == 0 and j == 0):
        if res[j][i][1] == "D":
            result_way.append("D")
            j -= 1
        else:
            result_way.append("R")
            i -= 1
    result_way = " ".join(result_way[::-1])
    return f"{res[-1][-1][0]}\n{result_way}"

if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        data = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    N, M = map(int, data.popleft().split())
    print(calculate(data, N, M))