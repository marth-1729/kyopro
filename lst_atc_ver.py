from atcoder import lazysegtree

inf = float("inf")

"""
遅延セグメント木
配列の長さをNとすると、主に次の処理を計算量 O(log N)
    ・配列のある区間にxを加算, 更新
    ・配列のある区間にモノイドを持つ演算(最大値 max, 和 sum など)を行う
"""


# ----------------------------------------------------------------------------------------------
# 区間最大値取得、区間加算
def LazySegmentTree(n):  # 遅延評価セグ木
    def op(l, r): return max(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)

    op_e = -inf  # モノイドの単位元

    def mapping(f, x): return f + x  # 遅延していたものを要素に反映させる関数

    def composition(f, g): return f + g  # 遅延操作を追加する関数

    comp_e = 0  # f@id=f, id@g=g となる写像の単位元
    data = [0] * n
    return lazysegtree.LazySegTree(op, op_e, mapping, composition, comp_e, data)


### 使用例 ###
size = 5
lazy_segtree = LazySegmentTree(size)  # 区間の長さが5の遅延セグメント木を作成

print("区間最大値取得, 区間加算")
lazy_segtree.apply(0, 1, 5)  # 半開区間[0, 1)の値を5加算
print(lazy_segtree.prod(0, 4))  # 半開区間[0, 4)で最大値5を出力
lazy_segtree.apply(0, 3, 6)  # 半開区間[0, 3) の値を6加算
print(lazy_segtree.all_prod())  # 全区間の最大値11を出力
print("\n")


# ----------------------------------------------------------------------------------------------
# 区間最小値取得、区間加算
def LazySegmentTree(n):  # 遅延評価セグ木
    def op(l, r): return min(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)

    op_e = inf  # モノイドの単位元

    def mapping(f, x): return f + x  # 遅延していたものを要素に反映させる関数

    def composition(f, g): return f + g  # 遅延操作を追加する関数

    comp_e = 0  # f@id=f, id@g=g となる写像の単位元
    data = [0] * n
    return lazysegtree.LazySegTree(op, op_e, mapping, composition, comp_e, data)


### 使用例 ###
size = 5
lazy_segtree = LazySegmentTree(size)  # 区間の長さが5の遅延セグメント木を作成

print("区間最小値取得, 区間加算")
lazy_segtree.apply(0, 4, 5)  # 半開区間[0, 4)の値を5加算
print(lazy_segtree.prod(2, 5))  # 半開区間[2, 5)で最小値0を出力
lazy_segtree.apply(0, 3, -6)  # 半開区間[0, 3)の値を-6加算
print(lazy_segtree.all_prod())  # 全区間の最小値-1出力
print("\n")


# ----------------------------------------------------------------------------------------------
# 区間和取得, 区間加算
def LazySegmentTree(n):  # 遅延評価セグ木
    from dataclasses import dataclass

    # 下のイテレータ？はちょっと重いから，一点取得は他のやつ使う方がいいかも
    @dataclass
    class V:
        value: int
        length: int


    def op(l, r): return V(l.value + r.value, l.length + r.length)  # 二項演算関数(区間最大: max, 区間和: sum など)

    op_e = V(0, 0)  # モノイドの単位元

    def mapping(f, x): return V(x.value + x.length * f, x.length)  # 遅延していたものを要素に反映させる関数


    def composition(f, g): return f + g  # 遅延操作を追加する関数


    comp_e = 0  # f@id=f, id@g=g となる写像の単位元
    data = [V(0, 1) for _ in range(n)]  # [値, 区間の長さ]
    return lazysegtree.LazySegTree(op, op_e, mapping, composition, comp_e, data)

### 使用例 ###
size = 5
lazy_segtree = LazySegmentTree(size)  # 区間の長さが5の遅延セグメント木を作成

print("区間和取得, 区間加算")
lazy_segtree.apply(0, 3, 5)  # 半開区間[0, 3)の値を5加算
print(lazy_segtree.prod(1, size).value)  # 半開区間[1, 5)の総和10を出力
lazy_segtree.apply(3, size, 6)  # 半開区間[3, 5) の値を6加算
print(lazy_segtree.all_prod().value)  # 全区間の総和27を出力
print("\n")


# ----------------------------------------------------------------------------------------------
# 区間最大値取得、区間更新
def LazySegmentTree(n):  # 遅延評価セグ木
    def op(l, r): return max(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)

    op_e = -inf  # モノイドの単位元

    def mapping(f, x): return x if f == comp_e else f  # 遅延していたものを要素に反映させる関数

    def composition(f, g): return g if f == comp_e else f  # 遅延操作を追加する関数

    comp_e = None  # f@id=f, id@g=g となる写像の単位元
    data = [0] * n
    return lazysegtree.LazySegTree(op, op_e, mapping, composition, comp_e, data)


### 使用例 ###
size = 5
lazy_segtree = LazySegmentTree(size)  # 区間の長さが5の遅延セグメント木を作成

print("区間最大値取得, 区間更新")
lazy_segtree.apply(0, 1, 5)  # 半開区間[0, 1)の値を5に更新
print(lazy_segtree.prod(0, 4))  # 半開区間[0, 4)で最大値5を出力
lazy_segtree.apply(0, 3, 6)  # 半開区間[0, 3) の値を6加算
print(lazy_segtree.all_prod())  # 全区間の最大値6を出力
print("\n")


# ----------------------------------------------------------------------------------------------
# 区間最小値取得、区間更新
def LazySegmentTree(n):  # 遅延評価セグ木
    def op(l, r): return min(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)

    op_e = inf  # モノイドの単位元

    def mapping(f, x): return x if f == comp_e else f  # 遅延していたものを要素に反映させる関数

    def composition(f, g): return g if f == comp_e else f  # 遅延操作を追加する関数

    comp_e = None  # f@id=f, id@g=g となる写像の単位元
    data = [0] * n
    return lazysegtree.LazySegTree(op, op_e, mapping, composition, comp_e, data)


### 使用例 ###
size = 5
lazy_segtree = LazySegmentTree(size)  # 区間の長さが5の遅延セグメント木を作成

print("区間最小値取得, 区間更新")
lazy_segtree.apply(0, 4, 5)  # 半開区間[0, 4)の値を5に更新
print(lazy_segtree.prod(2, size))  # 半開区間[2, 5)で最小値0を出力
lazy_segtree.apply(0, 3, -6)  # 半開区間[0, 3)の値を-6に更新
print(lazy_segtree.all_prod())  # 全区間の最小値-6出力
print("\n")


# ----------------------------------------------------------------------------------------------
# 区間bit反転，bitcount
def LazySegmentTree():  # 遅延評価セグ木


    def op(l, r):
        return V(l.zero + r.zero, l.one + r.one)  # 二項演算関数(区間最大: max, 区間和: sum など)

    op_e = V(0, 0)  # モノイドの単位元

    def mapping(f, x):
        if f == 1:
            return V(x.one, x.zero)  # 遅延していたものを要素に反映させる関数
        else:
            return V(x.zero, x.one)

    def composition(f, g):
        return (f + g) % 2  # 遅延操作を追加する関数

    comp_e = 0  # f@id=f, id@g=g となる写像の単位元
    # data = [V(0, 0) for _ in range(n)]  # [値, 区間の長さ]
    return lazysegtree.LazySegTree(op, op_e, mapping, composition, comp_e, data)

from dataclasses import dataclass


@dataclass
class V:
    zero: int
    one: int
A = [0, 1, 1, 0]
data = []
for a in A:
    if a == 1:
        data.append(V(0, 1))
    else:
        data.append(V(1, 0))

lazy_segtree = LazySegmentTree()
print(lazy_segtree.prod(0, 4))
lazy_segtree.apply(0, 3, 1)
print(lazy_segtree.prod(0, 4))