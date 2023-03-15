from collections import deque

def calculate(count_of_buyers, data):
    A = list()
    B = list()
    C = list()
    for _ in range(count_of_buyers):
        a, b, c = map(int, (data.popleft().split()))
        A.append(a)
        B.append(b)
        C.append(c)
    if count_of_buyers == 1:
        return f"{A[0]}"
    res = [0, A[0], min(A[0] + A[1], B[0])]
    for i in range(3, count_of_buyers + 1):
        min_ab = min(res[i - 1] + A[i - 1], res[i - 2] + B[i - 2])
        res.append(min(min_ab, res[i - 3] + C[i - 3]))
    return f"{res[-1]}"


if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        data = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    count_of_buyers = int(data.popleft().split()[0])
    with open('output.txt', 'w') as f_out:
        f_out.writelines(calculate(count_of_buyers, data))