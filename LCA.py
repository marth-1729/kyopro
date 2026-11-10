from collections import defaultdict, deque
import math

"""
link : https://github.com/marth-1729/kyopro/blob/main/LCA.py
ここのコードを改変・コピペで使用．
"""

# 2026/11/10 多少改良．
# 旧バージョンは，https://atcoder.jp/contests/abc014/submissions/80747068
# https://atcoder.jp/contests/abc014/tasks/abc014_4
#  -> ACコード：https://atcoder.jp/contests/abc014/submissions/80748086
# この問題はCPythonじゃないと通らなかった．(メモリ不足)
# PyPyでもTLEが怖い......
# 因みにLCA使わないけど，以下の問題では2*10 ^ 5 でもTLE
# https://atcoder.jp/contests/abc187/submissions/79828104
class LCA:
    """
    頂点 root を根とする木のLCAを構築．
    (想定)計算コスト：　Nは頂点数 (飽くまで)
        前処理：O(N logN)，
        計算　：O(logN).
    defaultdict を使っているので，多少計算量が重い．
    """

    def __init__(self, root, N):
        self.nn = 21        # TLE 回避用．
        self.ancient = [[0 for _ in range(N + 1)] for _ in range(self.nn + 1)]
        self.depth = [0] * (N + 1)
        ls = deque([(root, 0)])
        fin = {root}
        self.root = root
        self.depth[root] = 0
        while ls:
            cur, d = ls.popleft()
            for next in edges[cur]:
                if next in fin:
                    continue
                fin.add(next)
                self.ancient[0][next] = cur
                self.depth[next] = d + 1
                ls.append((next, d + 1))

        tmp = 1
        for _ in range(self.nn):
            self.bfs(tmp)
            tmp += 1

    def bfs(self, k):
        ls = deque([self.root])
        fin = {self.root}
        while ls:
            cur = ls.popleft()
            for next in edges[cur]:
                if next in fin:
                    continue
                # elif (k // 2, cur) in self.ancient:
                self.ancient[k][next] = self.ancient[k - 1][self.ancient[k - 1][next]]
                ls.append(next)
                fin.add(next)


    def calc(self, u, v):
        ans = 0
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        if self.depth[u] == 0:
            return (ans, u)

        M = int(math.log2(self.depth[u])) + 1
        num = 2 ** M
        for k in range(M, -1, -1):
            if self.depth[u] - self.depth[v] >= num:
                u = self.ancient[k][u]
                ans += num
            elif self.depth[u] - self.depth[v] == 0:
                break
            num //= 2

        if u == v:
            return (ans, v)

        M = int(math.log2(self.depth[u])) + 1
        for k in range(M, -1, -1):
            if self.ancient[k][u] != self.ancient[k][v]:
                u = self.ancient[k][u]
                v = self.ancient[k][v]
                ans += 2 ** (k + 1)

        return (ans + 2, self.ancient[0][u])

N = int(input())
edges = defaultdict(list)
for _ in range(N - 1):
    X, Y = map(int, input().split())
    edges[X].append(Y)
    edges[Y].append(X)

lca = LCA(1, N)
Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    ans, _ = lca.calc(a, b)
    print(ans + 1)

"""
使用例
"""
# https://onlinejudge.u-aizu.ac.jp/services/ice/
n = int(input())
edges = defaultdict(list)
for k in range(n):
    kk = list(map(int, input().split()))
    for c in range(1, kk[0] + 1):
        edges[k].append(kk[c])
        edges[kk[c]].append(k)
lca = LCA(0, n)
Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    print(lca.calc(u, v)[1])
