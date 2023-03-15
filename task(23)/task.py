from collections import deque

def calculate_steps(N):
    count_of_steps = [0, 0, 1, 1]
    prev_values = [0, 0, 1, 1]
    if N == 1:
        return f"0\n1"
    elif N == 2:
        return f"1\n1 2"
    elif N == 3:
        return f"1\n1 3"
    for i in range(4, N + 1):
        mn = 1000000
        if i % 3 == 0:
            mn = count_of_steps[i // 3]
        if i % 2 == 0:
            mn = min(mn, count_of_steps[i // 2])
        mn = min(count_of_steps[i - 1], mn)
        count_of_steps.append(mn + 1)
        if i % 3 == 0 and count_of_steps[i // 3] == mn:
            prev_values.append(i // 3)
        elif i % 2 == 0 and count_of_steps[i // 2] == mn:
            prev_values.append(i // 2)
        else:
            prev_values.append(i - 1)
    res = [N]
    prev = prev_values[N]
    count = count_of_steps[N]
    while count != 0:
        res.append(prev)
        prev = prev_values[prev]
        count = count_of_steps[prev]
    res.append(1)
    leng = len(res) - 1
    res = " ".join(list(map(str, res[::-1])))
    return f"{leng}\n{res}"


if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        N = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    N = int(N.popleft().split()[0])
    with open('output.txt', 'w') as f_out:
        f_out.writelines(calculate_steps(N))