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
        self.n = len(A)
        self.data = [0] * self.n
        self.func = func
        for i in range(self.n):
            self.add(i, A[i])

    def add(self, p, x):
        if self.func == "sum":
            assert 0 <= p < self.n
            p += 1
            while p <= self.n:
                self.data[p - 1] += x
                p += p & -p
        elif self.func == "xor":
            assert 0 <= p < self.n
            p += 1
            while p <= self.n:
                self.data[p - 1] ^= x
                p += p & -p

    def update(self, p, x):
        if self.func == "sum":
            assert 0 <= p < self.n
            self.add(p, x - self.data[p])

        elif self.func == "xor":
            assert 0 <= p < self.n
            self.add(p, x ^ self.data[p])


    def query(self, l, r):
        if self.func == "sum":
            return self.sum(l, r)
        elif self.func == "xor":
            return self.xor(l, r)

    def sum(self, l, r):
        assert 0 <= l <= r <= self.n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def xor(self, l, r):
        assert 0 <= l <= r <= self.n
        return self._xor(r) ^ self._xor(l)

    def _xor(self, r):
        s = 0
        while r > 0:
            s ^= self.data[r - 1]
            r -= r & -r
        return s

    def get(self, i):
        return self.sum(i, i + 1)

    def bisect_l(self, l, K):
        # \sum_{k = l} ^ {p} x_{k} >= K を満たす最小のpを返す．
        left = l; right = self.n + 1
        s = self._sum(l)
        while left < right:
            X = (left + right) // 2
            cur = self._sum(X + 1) - s
            if K > cur:
                left = X + 1
            else:
                right = X
        return left

    def bisect_r(self, r, K):
        # \sum_{k = p} ^ {N - 1}  x_{k} >= X を満たす最大のpを返す．
        left = -1; right = r
        s = self._sum(r + 1)
        while left < right:
            X = (left + right + 1) // 2
            cur = s - self._sum(X)
            if K <= cur:
                left = X
            else:
                right = X - 1
        return left


# 使用例1
n = 8
a = [0, 1, 2, 3, 4, 5, 6, 7]
fw = Fenwick_Tree(a, "xor")
print(fw.data)
print(fw.query(1, 3))
fw.add(1, 3)
print(fw.data)
print(fw.query(1, 3))


# 使用例2
n = 8
a = [0, 1, 2, 3, 4, 5, 6, 7]
fw = Fenwick_Tree(a, "sum")
print(fw.query(1, 3))
print(fw._sum(5))
print(fw.bisect_r(4, 4))
fw.add(1, 3)
print(fw.data)
print(fw.query(1, 3))
