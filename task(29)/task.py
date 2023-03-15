from collections import deque

inf = 1000000
dp = None
used = None
a = None

def DP(i, j):
    if j > i: return inf
    else:
        res = None
        cost = a[i]
        if j <= 0:
            if i >= 1:
                if cost <= 100:
                    res = min(DP(i - 1, j + 1), DP(i - 1, j) + cost)
                else:
                    return DP(i - 1, j + 1)
            else: 
                return 0
        else:
            if dp[i][j] != -1: 
                return dp[i][j]
            if cost > 100:
                res = min(DP(i - 1, j + 1), DP(i - 1, j - 1) + cost)
            else:
                res = min(DP(i - 1, j + 1), DP(i - 1, j) + cost)
        dp[i][j] = res
        return res


def Coupon_Days(i, j):
    if j < i:
        cost = a[i]
        if j <= 0:
            if i >= 1:
                if cost > 100 or DP(i - 1, j + 1) == DP(i, j):
                    used.append(i)
                    Coupon_Days(i - 1, j + 1)
                else:
                    Coupon_Days(i - 1, j)
        else:
            if DP(i - 1, j + 1) == DP(i, j):                    
                used.append(i)
                Coupon_Days(i - 1, j + 1)
            else:
                if cost <= 100:
                    Coupon_Days(i - 1, j)
                else:
                    Coupon_Days(i - 1, j - 1)


if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        d = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    n = int(d.popleft().split()[0])
    a = [0]
    for _ in range(1, n + 1): a.append(int(d.popleft().split()[0]))
    dp = [[] for _ in range(n + 1)]
    for i in range(n + 1):
        for _ in range(n + 2):
            dp[i].append(-1)

    ans = inf

    k1 = 0
    for i in range(n + 1):
        if ans >= DP(n, i):
            ans = DP(n, i)
            k1 = i

    used = []
    Coupon_Days(n, k1)

    k2 = len(used)

    answer = [str(ans), f"{k1} {k2}", "\n".join(map(str, sorted(used)))]
    with open('output.txt', 'w') as f_out:
        f_out.writelines("\n".join(answer))