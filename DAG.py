# https://atcoder.jp/contests/ndpc/tasks/ndpc2026_b
from collections import defaultdict
import sys

sys.setrecursionlimit(100000000)

"""
link :  https://github.com/marth-1729/kyopro/blob/main/DAG.py
ここのコードを改変・コピペで使用．
"""

T = int(input())


def dfs(u):
    for v in edges[u]:
        if v in ans:
            ans[u] += ans[v]
            continue
        dfs(v)
        ans[u] += ans[v]


for _ in range(T):
    N, M = map(int, input().split())
    edges = defaultdict(list)
    ans = defaultdict(int)
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
    ans[N] = 1
    dfs(1)
    print(ans[1] % 998244353)
