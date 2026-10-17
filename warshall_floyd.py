INF = float('inf')  # 無限大を表す値

def warshall_floyd(graph):
    """
    ワーシャル・フロイド法で全点対間最短経路を計算する

    Args:
        graph: 隣接行列形式のグラフ (2次元リスト)
               graph[i][j] は頂点iからjへの辺のコスト。
               辺が存在しない場合は INF。

    Returns:
        全点対間最短経路の距離行列 (2次元リスト)
    """
    n = len(graph)
    dist = [row[:] for row in graph]  # graph のコピーを作成

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# グラフの隣接行列表現 (0-indexed)
graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

result = warshall_floyd(graph)

# 結果の表示 (見やすく整形)
print("全点対間最短経路:")
for row in result:
    print(row)