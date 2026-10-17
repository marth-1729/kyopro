from collections import defaultdict


class Graph:
    def __init__(self, n: int):
        self.n = n
        self.adj = defaultdict(list)  # 隣接グラフ
        self.group = defaultdict(set)

    def add_edge(self, u, v):

        self.adj[u].append(v)
        self.adj[v].append(u)

    def make_non_weight_undirection_graph(self, vertex):
        """
        重み無しの無向グラフの作成
        引数　:tuple(要素数:2)のlist

        用途　:len(g[i])によって，頂点i の次数が分かる．
            　グラフの連結の仕方が分かる．
        """

        for i, j in vertex:
            self.adj[i].append(j)
            self.adj[j].append(i)

    def make_weight_undirection_graph(vertex):
        """
        重み付きの無向グラフの作成
        引数　:tuple(要素数:3)のlist

        用途　:len(g[i])によって，頂点i の次数が分かる．
            　グラフの連結の仕方が分かる．
        """
        maked_g = defaultdict(list)
        for i, j, k in vertex:
            maked_g[i].append((j, k))
            maked_g[j].append((i, k))
        return maked_g

    def make_non_weight_direction_graph(vertex):
        """
        重み無しの有向グラフの作成
        引数　:tuple(要素数:2)のlist

        用途　:len(g[i])によって，頂点i の次数が分かる．
            　グラフの連結の仕方が分かる．
        """
        maked_g = defaultdict(list)
        for i, j in vertex:
            maked_g[i].append(j)
        return maked_g

    def make_weight_direction_graph(vertex):
        """
        重み付きの有向グラフの作成
        引数　:tuple(要素数:3)のlist

        用途　:len(g[i])によって，頂点i の次数が分かる．
            　グラフの連結の仕方が分かる．
        """
        maked_g = defaultdict(list)
        for i, j, k in vertex:
            maked_g[i].append((j, k))
        return maked_g

    def union(self, i: int, j: int):
        self.group[i] |= {self.group[j]}
        return


"""
N=int(input())
uv=[]

for i in range(N-1):
    u,v,w=map(int,input().split())
    uv.append((u,v,w))

print(uv)
"""
g = Graph(10)
g.add_edge(1, 3)
a = defaultdict(int)
# g.make_non_weight_undirection_graph([(2,3),(3,5)])
print(g.adj)


