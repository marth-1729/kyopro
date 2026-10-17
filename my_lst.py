from atcoder import lazysegtree
import operator
import math

inf = float("inf")

"""
遅延セグメント木
配列の長さをNとすると、主に次の処理を計算量 O(log N)
    ・配列のある区間にxを加算, 更新
    ・配列のある区間にモノイドを持つ演算(最大値 max, 和 sum など)を行う
"""

def LazySegmentTree(n, def_opration, def_map):  # 遅延評価セグ木
    """
    memo
    引数 n             : 適応リストのデータ数
    　　　def_opration : 取得したい区間への関数 (今のところ，maxとmin しか使えない)
         def_map      : 更新したい区間への関数 (add, mul は使えるカモ)
    """


    from dataclasses import dataclass

    @dataclass
    class V:
        value: int
        length: int


    if def_opration == "min":
        op_e = inf  # モノイドの単位元
        def op(l, r):
            return min(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)

    elif def_opration == "max":
        op_e = -inf  # モノイドの単位元
        def op(l, r):
            return max(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)

    elif def_opration == "add":
        op_e = V(0, 0)
        def op(l, r):
            return V(l.value + r.value, l.length + r.length)

    elif def_opration == "mul":
        op_e = V(1, 1)
        def op(l, r):
            return V(l.value * r.value, l.value * r.value)
    else:
        op_e = inf  # モノイドの単位元
        def op(l, r):
            return min(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)


    if def_map == "min":
        comp_e = inf  # モノイドの単位元
        def mapping(f, x):
            return min(f, x)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)

        def composition(f, g):
            return min(f, g)  # 遅延操作を追加する関数

    elif def_map == "max":
        comp_e = -inf  # モノイドの単位元
        def mapping(f, x):
            return max(f, x)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)

        def composition(f, g):
            return max(f, g)  # 遅延操作を追加する関数

    elif def_map == "add":
        comp_e = 0
        def mapping(f, x):
            return f + x
        def composition(f, g):
            return f + g  # 遅延操作を追加する関数

    elif def_map == "mul":
        comp_e = 1
        def mapping(f, x):
            return f * x
        def composition(f, g):
            return (f * g)  # 遅延操作を追加する関数
    else:
        op_e = inf  # モノイドの単位元
        def mapping(f, x):
            return min(f, x)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)

        def composition(f, g):
            return min(f, g)  # 遅延操作を追加する関数



    data = [0] * n
    return lazysegtree.LazySegTree(op, op_e, mapping, composition, comp_e, data)

lst=LazySegmentTree(5, "mul", "mul")
lst.set(0,1)
lst.set(1,3)
lst.set(2,9)
lst.set(3,3)
lst.set(4,5)
lst.apply(1,5,2)
print(lst.prod(2,4))