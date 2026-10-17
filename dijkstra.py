import sys
import heapq

sys.setrecursionlimit(10 ** 9)
def dijkstra(graph, start):
    # 初期化
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0
    pq = [(0, start)]

    # ダイクストラ法
    while pq:
        # 未処理の中で最小の距離を持つ頂点を取り出す
        dist, u = heapq.heappop(pq)
        if visited[u]:
            continue

        # 訪問済みにする
        visited[u] = True

        # uから到達可能な頂点の距離を更新する
        for v, weight in graph[u]:
            if not visited[v]:
                new_distance = distance[u] + weight
                if new_distance < distance[v]:
                    distance[v] = new_distance
                    heapq.heappush(pq, (new_distance, v))

    return distance


# ex 1.
graph = [
    [(1, 2), (2, 4)],
    [(0, 2), (2, 1), (3, 4)],
    [(0, 4), (1, 1), (3, 1), (4, 3)],
    [(1, 4), (2, 1), (4, 1)],
    [(2, 3), (3, 1)]
]

start = 0
distance = dijkstra(graph, start)
print(distance) # [0, 2, 3, 5, 6]


# ex 2. ABC340 D問題
import sys
import heapq

sys.setrecursionlimit(10 ** 9)

def dijkstra(graph, start):
    # 初期化
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0
    pq = [(0, start)]

    # ダイクストラ法
    while pq:
        # 未処理の中で最小の距離を持つ頂点を取り出す
        dist, u = heapq.heappop(pq)
        if visited[u]:
            continue

        # 訪問済みにする
        visited[u] = True

        # uから到達可能な頂点の距離を更新する
        for v, weight in graph[u]:
            if not visited[v]:
                new_distance = distance[u] + weight
                if new_distance < distance[v]:
                    distance[v] = new_distance
                    heapq.heappush(pq, (new_distance, v))

    return distance

N=int(input())
graph=[]
for i in range(N-1):
    g=[]
    A,B,X=map(int,input().split())
    g.append((i+1,A))
    g.append((X-1,B))
    graph.append(g)

graph.append([])
dis=dijkstra(graph,0)
print(dis[-1])



# bellman ford 法
def bellman_ford(edges, start):
    # 頂点数
    n = len(edges)

    # 初期化
    dist = [float('inf')] * n
    dist[start] = 0

    # 辺の緩和
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    # 負のサイクルの検出
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + w:
            raise ValueError('Negative cycle detected')

    return dist

# グラフの例
graph = {
    0: [(1, 4), (2, 3)],
    1: [(2, -2), (3, 1)],
    2: [(3, 2)],
    3: []
}

# 始点を0として実行
distances = bellman_ford([(u, v, w) for u, edges in graph.items() for v, w in edges], start=0)

# 結果の出力
print(distances)