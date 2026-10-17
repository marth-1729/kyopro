from atcoder.scc import SCCGraph

"""
強連結成分：
グラフGのうち，互いに行き来できるような頂点集合のこと．

これを行うことにより，トポロジカルソート(グラフの頂点にも順序付け)ができる
計算コスト：O(| E | + | V |) , | E | : 辺の数，| G | : 頂点の数


"""

N, M = map(int, input().split())
graph = SCCGraph(N)
for _ in range(M):
    a, b = map(int, input().split())
    graph.add_edge(a, b)

groups = graph.scc()
print(len(groups))
for group in groups:
    print(len(group), *group)
