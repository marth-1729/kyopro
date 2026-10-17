from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N, u, v = map(int,input().split())
edges = defaultdict(list)
for _ in range(N-1):
    A, B = map(int,input().split())
    edges[A].append(B)
    edges[B].append(A)

root = [u]
fin = [False] * N
fin[u - 1] = True
flag = False
def dfs(u, v):
    global flag
    for next in edges[u]:
        if fin[next - 1]:
            continue
        if flag:
            return
        root.append(next)
        if next == v:
            flag = True
            return
        else:
            fin[next - 1] = True
            dfs(next, v)
    if flag:
        return
    root.pop()
dfs(u, v)
