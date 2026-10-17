from collections import defaultdict


# membersとかは，呼び出し時に頂点をlistに入れていくので，計算量コストがかかる
class UnionFind:

    def __init__(self, n):
        """
        UnionFindの初期化
        値が負となる頂点が親頂点．
        """

        self.n = n
        self.parents = [-1] * n #これが親頂点の次数&各頂点の親頂点を表している．
        self.cycle = 0

    def find(self, x):
        """
        引数  : x(頂点)
        戻り値: 頂点 x の親頂点を返す．
        """

        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        引数  : x, y　(頂点)
        操作　: 2頂点 x, y の親頂点をどちらかに合わせる．
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            self.cycle += 1
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        引数　: x　(頂点)
        戻り値: 頂点 x が何個の頂点と連結しているか．
               換言すると，頂点 x が属する連結成分 1 のグラフの頂点数．
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """
        引数  : x, y　(頂点)
        戻り値: 2頂点 x, y の親頂点が同じかどうか．
        　　　　換言すると，2頂点 x, y が同じグループかどうか．(True or False)
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        引数  : x　(頂点)
        戻り値: 頂点xと同じグループの頂点のリスト．
               換言すると，頂点 x が属する連結成分 1 のグラフの頂点のリスト．
        コスト： x と同じグループ数
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root] # 内包表記

    def roots(self):
        """
        引数　: 無し
        戻り値: グラフの親頂点のリスト．
        """
        return [i for i, x in enumerate(self.parents) if x < 0] # enumurate関数は，defaultdictに適応できないらしい...

    def group_count(self):
        """
        引数　: 無し
        戻り値: グラフの連結成分．
        """
        return len(self.roots())

    def all_group_members(self):
        """
        引数　: 無し
        戻り値: 各親頂点に連結している頂点の状態．
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def add_edge(self, n):
        """
        引数　: n (新しく追加したい頂点の個数)
        """
        add_edge = [-1] * n
        self.n += n
        self.parents += add_edge

uf=UnionFind(10)
uf.union(2,3)
uf.union(3, 7)
print(uf.roots())
print(uf.find(2))
print(uf.all_group_members())
uf.add_edge(3)
print(uf.all_group_members())