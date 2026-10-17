from collections import defaultdict
from collections import deque


def tree_distance(n: int, adj: defaultdict, r: int) -> tuple:
    d = [0] * (n + 1)  # rからの距離．1-index
    checked = [False] * (n + 1)  # チェック済み判定．1-index
    q = deque([r])  # これから探索する点を格納するキュー
    d[r] = 0
    checked[r] = True
    max_d, max_v = 0, r  # rからの最大距離．最大距離の点
    while q:
        v = q.popleft()
        for u, c in adj[v]:  # 隣接点，(v, u)の距離
            if not checked[u]:
                d[u] = d[v] + c
                if d[u] > max_d:
                    max_d, max_v = d[u], u
                checked[u] = True
                q.append(u)
    return max_v, max_d, d  # rから最も遠い点，rから最も遠い距離，距離（リスト）


def tree_diameter(n: int, adj: defaultdict):
    max_v1, max_d1, d1 = tree_distance(n, adj, 1)
    max_v2, max_d2, d2 = tree_distance(n, adj, max_v1)
    return max_d2


N = 4
ABC = [(1, 2, 2), (1, 3, 3), (1, 4, 4)]  # (端点1，端点2，距離）．木なので枝数は N-1
adj = defaultdict(list)
for a, b, c in ABC:
    adj[a].append((b, c))  # (隣接点，距離）
    adj[b].append((a, c))
print(tree_diameter(N, adj))  # 直径は 点[3,1,4]を通る 7
