from collections import deque

def calculate(data):
    n = int(data.popleft().split()[0])
    a = list(map(int, data.popleft().split()))
    res = [0 for _ in range(n)]
    a.sort()
    if n == 2:
        return str(abs(a[1] - a[0]))
    else:
        res[1] = a[1] - a[0]
        res[2] = a[2] - a[0]
        for i in range(3, n):
           res[i] = min(res[i - 1], res[i - 2]) + a[i] - a[i - 1]

    return str(res[-1])


if __name__ == "__main__":
    with open('input.txt', 'r') as f_in:
        data = deque(
            line.rstrip()
            for line in f_in.readlines()
        )

    print(calculate(data))