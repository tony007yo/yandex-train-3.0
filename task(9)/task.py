def calc_matr_sum(matr, x1, x2, y1, y2):
    return matr[x2][y2] - matr[x1][y2] - matr[x2][y1] + matr[x1][y1]

def prefixsum(matr_rsq, n, m):    
    # horizontal prefixsum
    for i in range(1, n):
        nums_line = list(map(int, input().split()))
        for j in range(1, m):
            matr_rsq[i][j] = matr_rsq[i][j - 1] + nums_line[j - 1]
    
    # vertical prefixsum
    for j in range(1, m):
        for i in range(1, n):
            matr_rsq[i][j] = matr_rsq[i - 1][j] + matr_rsq[i][j]
         
N, M, K = map(int, input().split())
matr_rsq = [[0] * (M + 1) for _ in range(N + 1)]
prefixsum(matr_rsq, N + 1, M + 1)
ans= []
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    ans.append(calc_matr_sum(matr_rsq, x1 - 1, x2, y1 - 1, y2))
print('\n'.join(map(str, ans)))