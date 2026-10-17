import sys

sys.setrecursionlimit(100000000)

input = sys.stdin.readline  # EOFのやつ．


def fib(a1, a2, rep):
    tmp = a1
    a1 = a2
    a2 = tmp + a1
    rep -= 1
    if rep > 0:
        a2 = fib(a1, a2, rep)
    print(locals())  # デバッグ用
    return a2


a, b, c = map(int, input().split())
ans = fib(a, b, c)
print(ans)
