# 解の二分探索
# 個人的に苦手意識があったので，残しておく．
# 恐らく，ようかんパーティーも同じ解法

def bisect_solution(left, right, K):
    if left == right:
        print(left)
        exit()
    X = (left + right + 1) // 2
    cnt = 0
    cur = 0
    for i in range(len(A)):
        if A[i] + cur >= X:
            cnt += 1
            cur = 0
        else:
            cur += A[i]
    if K <= cnt:
        bisect_solution(X, right, K)
    else:
        bisect_solution(left, X - 1, K)


N, K = map(int, input().split())
A = list(map(int, input().split()))
A_sum = sum(A) // K
bisect_solution(0, A_sum, K)


# list の二分探索も置いとく．（SegTree で応用できそう）
ls = [0] * N
def bisect_list(left, right, K):
    while left < right:
        X = (left + right + 1) // 2
        cur = ls[X]
        if K > cur:
            left = X
        else:
            right = X - 1
    return left