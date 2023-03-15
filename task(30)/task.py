n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
dp = []
for i in range(n + 1):
    dp.append([0] * (m + 1))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if b[j - 1] == a[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
res = []
i = n
j = m
while j != 0 and i != 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        res.append(a[i - 1])
        i -= 1
        j -= 1
print(*res[::-1])