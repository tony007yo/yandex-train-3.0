def calculate(N, k):
    if k == 1:
        return k
    l = list()
    l.append(1)
    
    k = min(N,k)
    N = max(N,k)
    
    flag = k
    for i in range(1, k):
        res = 0
        for j in range(1, k):
            if i - j >= 0:
                res += l[i - j]
            else:
                break
        l.append(res)
        if flag > 0:
            l[i] += 1
            flag -= 1

    for i in range(k, N):
        res = 0
        for j in range(1, k + 1):
            if i - j >= 0:
                res += l[i - j]
            else:
                break
        l.append(res)
    return l[N - 2]

if __name__ == '__main__':
    N, k = map(int, input().split())
    print(calculate(N, k))