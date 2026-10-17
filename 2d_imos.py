# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i
# 2D_imos 苦手なので作成．

H, W, N = map(int, input().split())
imos = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    imos[A - 1][B - 1] += 1
    imos[A - 1][D] -= 1
    imos[C][B - 1] -= 1
    imos[C][D] += 1

for i in range(H):
    cur = 0
    for j in range(W):
        cur += imos[i][j]
        imos[i][j] = cur

for j in range(W):
    cur = 0
    for i in range(H):
        cur += imos[i][j]
        imos[i][j] = cur

for i in range(H):
    print(*imos[i][:-1])
