def LU(A, n):
    # n 次行列 A を LU分解する．

    L = [[0 for _ in range(n)] for _ in range(n)]
    U = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        U[0][i] = A[0][i]

    for i in range(n):
        for j in range(i, n):
            if i == j:
                L[i][i] = 1
            else:
                for k in range(i):
                    L[j][i] -= L[j][k] * U[k][i]
                L[j][i] += A[j][i]
                if U[i][i] == 0:
                    U[i][i] += 10 ** (-10)
                L[j][i] /= U[i][i]

            if i == 0:
                continue

            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]
            U[i][j] += A[i][j]

    return (L, U)

def sim_equ(A, b):
    # 連立方程式 Ax = b の解 x を求める．(A は，n 次正方行列　かつ　フルランク)．det のアルゴリズムを勉強したら追記予定．
    # コスト：O(n ^ 3)，

    """
    方針: A = LU として，y := Ux とおき，
            Ly = LUx = b を解く．
    ➀ Ly = b を解く．L は下三角なので yは求まる．
    ➁ Ux = y を解く．U は上三角なので xは求まる．
    """
    n = len(A)
    L, U = LU(A, n)
    y = [0] * n
    x = [0] * n

    # ➀ Ly = b を解く．
    for i in range(n):
        exc = b[i]
        for j in range(i):
            exc -= L[i][j] * y[j]
        y[i] = exc / L[i][i]

    # ➁ Ux = y を解く．
    for i in range(n):
        exc = y[- i - 1]
        for j in range(i):
            exc -= U[- i - 1][- j - 1] * x[- j - 1]

        if U[- i - 1][- i - 1] == 0:
            x[- i - 1] = exc / (U[- i - 1][- i - 1] + 10 ** (- 10))
        else:
            x[- i - 1] = exc / U[- i - 1][- i - 1]

    return x

A = [[1, 1, 1], [2, 3, -2], [3, -1, 1]]
n = 3

# LU分解の使用例
print("LU 分解")
L, U = LU(A, n)
print("出力")
print("L = ")
for i in range(n):
    print(*L[i])
print()
print("U = ")
for i in range(n):
    print(*U[i])
print()
print("入力")
print("A = ")
for i in range(n):
    print(*A[i])
print()
ans = []
print("A = LU となっているか確認")
print("LU = ")
for i in range(n):
    add = []
    for j in range(n):
        num = 0
        for k in range(n):
            num += U[k][j] * L[i][k]
        add.append(num)
    ans.append(add)

for i in range(n):
    print(*ans[i])

# sim_equの使用例
# 解が一意に定まる Ax = b の解を求める関数
A = [[1, 1, 1], [2, 3, -2], [3, -1, 1]]
n = 3
b = [9, 5, 7]
ans = sim_equ(A, b)
print("x =", ans)
print("検算")
# 検算の表示部
for i in range(n):
    a = 0
    for j in range(n):
        a += A[i][j] * ans[j]
        if A[i][j] < 0:
            print("(", A[i][j], ")", end="")
        else:
            print(A[i][j], end="")
        print(" * ", end="")
        if ans[j] < 0:
            print("(", ans[j], ")", end="")
        else:
            print(ans[j], end="")
        if j != n - 1:
            print(" + ", end="")
    print(" =", a)
print("b =", b)

"""
def matrix_multi(A, B):

    A_row = len(A)
    A_column = len(A[0])
    B_row = len(B)
    B_column = len(B[0])
    ans = []
    for i in range(A_column):
        add = []
        for j in range(B_row):
            num = 0
            for k in range(A_column):
                num += A[k][j] * B[i][k]
            add.append(num)
        ans.append(add)

    return ans

L, U = LU(A, n)
a = matrix_multi(L, U)
for i in range(4):
    print(*a[i])
"""