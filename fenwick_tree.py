"""
link : https://github.com/marth-1729/kyopro/blob/main/fenwick_tree.py
ここのコードを改変・コピペで使用．
"""

# 参考(改造)：https://qiita.com/AkariLuminous/items/f2f7930e7f67963f0493

"""
Fenwick Tree

できることはSeg木とほぼ同じ．
一点更新  ：O(log N)
区間クエリ：O(log N)

考え方は累積和と近い．
「+」と「xor」なら，Fenwick Treeを使う．
逆元の存在が担保されていたら使える．

コメント：ACLのFenwick Treeだと，加法しかできないので，多作のライブラリをもらう．
        のちのちは，他の演算や二次元のものも勉強したい．(わかりやすいサイトとかないかな......)
"""
class Fenwick_Tree:
    # 今のところは，sumとxorのみ．
    def __init__(self, A, func = "sum"):
        self._n = len(A)
        self.data = A
        self.func = func

    def add(self, p, x):
        if self.func == "sum":
            assert 0 <= p < self._n
            p += 1
            while p <= self._n:
                self.data[p - 1] += x
                p += p & -p
        elif self.func == "xor":
            assert 0 <= p < self._n
            p += 1
            while p <= self._n:
                self.data[p - 1] ^= x
                p += p & -p

    def update(self, p, x):
        if self.func == "sum":
            assert 0 <= p < self._n
            self.add(p, x - self.data[p])
            # p += 1
            # while p <= self._n:
            #     self.data[p - 1] += x
            #     p += p & -p
        elif self.func == "xor":
            assert 0 <= p < self._n
            self.add(p, x ^ self.data[p])
            # pp = p + 1
            # pre = self.date[p]
            # while p <= self._n:
            #     self.data[p - 1] -= pre
            #     pp += pp & -pp
            # p += 1
            # while p <= self._n:
            #     self.data[p - 1] ^= x
            #     p += p & -p

    def query(self, l, r):
        if self.func == "sum":
            return self.sum(l, r)
        elif self.func == "xor":
            return self.xor(l, r)

    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def xor(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._xor(r) ^ self._xor(l)

    def _xor(self, r):
        s = 0
        while r > 0:
            s ^= self.data[r - 1]
            r -= r & -r
        return s

# 使用例
n = 8
a = [0, 1, 2, 3, 4, 5, 6, 7]
fw = Fenwick_Tree(a, "xor")
print(fw.data)
print(fw.query(1, 3))
fw.add(1, 3)
print(fw.data)
print(fw.query(1, 3))
