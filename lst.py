"""
遅延セグメント木
配列の長さをNとすると，主に次の処理を計算量 O(log N)
    ・配列のある区間にxを加算，更新
    ・配列のある区間にモノイドを持つ演算(最大値 max，和 sum など)を行う
"""

# 写経はまだしてない．使用感試してみる．
class LazySegmentTree:
    """
    区間更新，区間取得を行う場合に有効なデータ構造

    データ構造の作成    : O(NlogN)
    データの更新       : O(logN)
    データの取得       : O(1)

    できること
    ・データの区間更新
    ・データの区間取得
    """

    """
    説明書(LazySegTreeの部分は--と記載)
    ・--.set(p, x)        : p番目のデータを xに更新(一点更新)．O(log n)
    ・--.get(p)           : p番目のデータを取得(一点取得)．O(log n)
    ・--.prod(l, r)       : 半開区間 [l, r) において，op で定義した演算結果(区間取得)． O(log n)
    ・--.all_prod(l, r)   : 全区間 [0, len(適応リスト)) において，op で定義した演算結果(区間取得)． O(1)
    ・--.apply(f)         : p番目のデータに対し，mapping で定義した演算を適応(一点更新)． O(log n)
    ・--.apply_lr(l, r, f): 半開区間 [l, r) において，op で定義した演算を適応(区間更新)． O(log n)
    
    以下の2つは未解読．
    ・--.max_right(l, g)  : 
    ・--.min_left(r, g)   : 
    """

    def __init__(self, op, e, mapping, composition, id,
                 n: int = -1, data: list = []):
        """
        初期化 (計算量 : O(n))

        Parameters
        ----------
        op :
            結合法則を満たす、区間から取得したい演算

        e : opで定義した演算に対する単位元

        mapping :
            遅延していた更新情報を各要素に伝搬させる演算

        composition :
            遅延していた更新情報が重複したときの合成関数

        id :
            mappingで定義した演算の単位元

        Raises
        ------
        AssertionError
            ・assert len(data) or (n > 0)
                LazySegmentTreeを構築する元になるリストの大きさが0より小さい場合
        """

        assert (len(data) > 0) or (n > 0)
        if (len(data) == 0):
            data = [e] * n
        self.__n = len(data)
        self.__log = (self.__n - 1).bit_length()
        self.__size = 1 << self.__log
        self.__d = [e] * (2 * self.__size)
        self.__lz = [id] * self.__size
        self.__op = op
        self.__e = e
        self.__mapping = mapping
        self.__composition = composition
        self.__id = id

        for i in range(self.__n):
            self.__d[self.__size + i] = data[i]
        for i in range(self.__size - 1, 0, -1):
            self.__update(i)

    def __update(self, k: int):
        """ 内部の処理で用いているだけなので使用しない """
        self.__d[k] = self.__op(self.__d[2 * k], self.__d[2 * k + 1])

    def __all_apply(self, k: int, f):
        """ 内部の処理で用いているだけなので使用しない """
        self.__d[k] = self.__mapping(f, self.__d[k])
        if (k < self.__size):
            self.__lz[k] = self.__composition(f, self.__lz[k])

    def __push(self, k: int):
        """ 内部の処理で用いているだけなので使用しない """
        self.__all_apply(2 * k, self.__lz[k])
        self.__all_apply(2 * k + 1, self.__lz[k])
        self.__lz[k] = self.__id

    def set(self, p: int, x):
        """
        LazySegmentTreeを構築する元になったリストのp番目の値をxに更新する
        (計算量 : O(log n))

        Parameters
        ----------
        p : int
            元のリストの更新したい要素のインデックス

        x : 型の指定なし
            更新させたいデータ

        Raises
        ------
        AssertionError
            ・assert (0 <= p) and (p < self.__n)
                指定したpが元のリストで配列外参照を起こす場合

        Example
        -------
        A : [0, 0, 0]

            ↓  set(1, 5)

        A : [0, 5, 0]
        """

        assert (0 <= p) and (p < self.__n)
        p += self.__size
        for i in range(self.__log, 0, -1):
            self.__push(p >> i)
        self.__d[p] = x
        for i in range(1, self.__log + 1):
            self.__update(p >> i)

    def get(self, p: int):
        """
        LazySegmentTreeを構築する元になったリストのp番目の値を取得
        (計算量 : O(log n))

        Parameter
        ---------
        p : int
            元のリストの取得したい要素のインデックス

        Raises
        ------
        AssertionError
            ・assert (0 <= p) and (p < self.__n)
                指定したpが元のリストで配列外参照を起こす場合

        Example
        -------
        A : [1, 2, 3]

        get(1) = 2
        """

        assert (0 <= p) and (p < self.__n)
        p += self.__size
        for i in range(self.__log, 0, -1):
            self.__push(p >> i)
        return self.__d[p]

    def prod(self, l: int, r: int):
        """
        LazySegmentTreeを構築する元になったリストの半開区間[l, r)に対して，
        opで定義した演算の結果を取得 (計算量 : O(log n))

        Parameters
        ----------
        l : int
            半開区間の左端のインデックス

        r : int
            半開区間の右端のインデックス

        Raises
        ------
        AssertionError
            ・assert (0 <= l) and (l <= r) & (r <= self.__n)
                指定したl, rが配列外参照を起こす、またはr < lとなる場合

        Example
        -------
        A : [2, 1, 4, 3, 5], op : max

        prod(0, 2) = 1
        """

        assert (0 <= l) and (l <= r) & (r <= self.__n)
        if (l == r):
            return self.__e

        l += self.__size
        r += self.__size

        for i in range(self.__log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push(r >> i)

        sml = self.__e
        smr = self.__e
        while (l < r):
            if (l & 1):
                sml = self.__op(sml, self.__d[l])
                l += 1
            if (r & 1):
                r -= 1
                smr = self.__op(self.__d[r], smr)
            l //= 2
            r //= 2

        return self.__op(sml, smr)

    def all_prod(self):
        """
        LazySegmentTreeを構築する元になったリストの
        全区間に対して、opで定義した演算の結果を取得 (計算量 : O(1))

        Parameter
        ---------
        無し

        Example
        -------
        A : [2, 1, 4, 3, 5], op : sum

        all_prod() = 15
        """
        return self.__d[1]

    def apply(self, p: int, f):
        """
        LazySegmentTreeを構築する元になったリストのp番目の要素に対して，
        mappingで定義した演算を適用する (計算量 : O(log n))

        Parameters
        ----------
        p : int
            更新したい元のリストの要素のインデックス

        f : 型の指定なし(op, mapping, compositionに依存)
            作用させたいデータ

        Raises
        ------
        AssertionError
            ・assert (0 <= p) and (p < self.__n)
                指定したpが元のリストで配列外参照を起こす場合

        Example
        -------
        A : [a1, a2, a3, a4, a5], mapping(f, a1) : f*x

            ↓  apply(1, f)

        A : [a1, 2*a2, a3, a4, a5]
        """

        assert (0 <= p) and (p < self.__n)
        p += self.__size
        for i in range(self.__log, 0, -1):
            self.__push(p >> i)
        self.__d[p] = self.__mapping(f, self.__d[p])
        for i in range(1, self.__log + 1):
            self.__update(p >> i)

    # 区間適用
    def apply_lr(self, l: int, r: int, f):
        """
        LazySegmentTreeを構築する元になったリストの半開区間[l, r)に対して，
        mappingで定義した演算を適用する (計算量 : O(log n))

        Parameters
        ----------
        l : int
            半開区間の左端のインデックス

        r : int
            半開区間の右端のインデックス

        f : 型の指定なし(op, mapping, compositionに依存)
            作用させたいデータ

        AssertionError
            ・assert (0 <= l) and (l <= r) and (r <= self.__n)
                指定したl, rが配列外参照を起こす、またはr < lとなる場合

        Example
        -------
        A : [a1, a2, a3, a4, a5], mapping(f, a1) : f*x

            ↓  apply_lr(2, 5, 2)

        A : [a1, a2, 2*a3, 2*a4, 2*a5]
        """

        assert (0 <= l) and (l <= r) and (r <= self.__n)
        if (l == r):
            return

        l += self.__size
        r += self.__size

        for i in range(self.__log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push((r - 1) >> i)

        l2, r2 = l, r
        while (l < r):
            if (l & 1):
                self.__all_apply(l, f)
                l += 1
            if (r & 1):
                r -= 1
                self.__all_apply(r, f)
            l //= 2
            r //= 2
        l, r = l2, r2

        for i in range(1, self.__log + 1):
            if ((l >> i) << i) != l:
                self.__update(l >> i)
            if ((r >> i) << i) != r:
                self.__update((r - 1) >> i)

    def max_right(self, l: int, g) -> int:
        """
        g(op(a[l], a[l + 1], ..., a[r - 1])) = true
        となる最大のrを取得 (計算量 : O(log n))

        Parameters
        ----------
        l : int
            半開区間の左端となるインデックス

        g : 関数
            bool値を返す関数

        Raises
        ------
        AssertionError
            ・assert (0 <= l) and (l <= self.__n)
                配列外となるlを指定した場合

            ・assert g(self.__e)
                単位元でgの条件がfalseとなるgを引数として受け取った場合

        Returns
        -------
        r : int
            gで定義された条件を半開区間[l, r)で全て満たすr

        Notes
        -----
        l = r となるようなrが返り値として与えられたとき場合、
        条件を満たすようなrが存在しないことを表す

        Example
        -------
        A : [3, 2, 1, 3, 4, 5], g(x) : x <= 2

        max_right(1, g) = 3
        (半開区間[1, r)の最大値が2以下となるようなrの最大値は3)

        max_right(0, g) = 0
        (半開区間[0, r)の最大値が2以下となるようなrは存在しない)
        """

        assert (0 <= l) and (l <= self.__n)
        assert g(self.__e)
        if (l == self.__n):
            return self.__n
        l += self.__size
        for i in range(self.__log, 0, -1):
            self.__push(l >> i)
        sm = self.__e
        while (True):
            while (l % 2 == 0):
                l //= 2
            if (not g(self.__op(sm, self.__d[l]))):
                while (l < self.__size):
                    self.__push(l)
                    l *= 2
                    if (g(self.__op(sm, self.__d[l]))):
                        sm = self.__op(sm, self.__d[l])
                        l += 1
                return l - self.__size
            sm = self.__op(sm, self.__d[l])
            l += 1
            if (l & -l) == l:
                break
        return self.__n

    def min_left(self, r: int, g):
        """
        g(op(a[l], a[l + 1], ..., a[r - 1])) = true
        となる最大のlを取得 (計算量 : O(log n))

        Parameters
        ----------
        r : int
            半開区間の左端となるインデックス

        g : 関数
            bool値を返す関数

        Raises
        ------
        AssertionError
            ・assert (0 <= r) and (r <= self.__n)
                指定したrが元のリストで配列外参照を起こす場合

            ・assert g(self.__e)
                単位元でgの条件がfalseとなるgを引数として受け取った場合

        Returns
        -------
        l : int
            gで定義された条件を半開区間[l, r)で全て満たすl

        Notes
        -----
        l = r となるようなlが返り値として与えられたとき場合、
        条件を満たすようなlが存在しないことを表す

        Example
        -------
        A : [3, 2, 1, 3, 4, 5], g(x) : x <= 3

        min_left(4, g) = 0
        (半開区間[l, r)の最大値が3以下となるようなlは0)

        min_left(6, g) = 6
        (半開区間[l, r)の最大値が3以下となるようなlは存在しない)
        """
        assert (0 <= r) and (r <= self.__n)
        assert g(self.__e)
        if (r == 0):
            return 0
        r += self.__size
        for i in range(self.__log, 0, -1):
            self.__push((r - 1) >> i)
        sm = self.__e
        while (True):
            r -= 1
            while (r > 1) & (r % 2):
                r //= 2
            if (not g(self.__op(self.__d[r], sm))):
                while (r < self.__size):
                    self.__push(r)
                    r = 2 * r + 1
                    if (g(self.__op(self.__d[r], sm))):
                        sm = self.__op(self.__d[r], sm)
                        r -= 1
                return r + 1 - self.__size
            sm = self.__op(self.__d[r], sm)
            if (r & -r) == r:
                break
        return 0



# 使用例

# 区間最大値取得、区間加算
def seg_func(n: int):
    inf = float("inf")
    def op(l: int, r: int): return max(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)
    op_e = -inf  # 二項演算・の単位元
    def mapping(f: int, x: int): return f + x  # 遅延していたものを要素に反映させる関数
    def composition(f: int, g: int): return f + g  # 遅延操作を追加する関数
    comp_e = 0  # f@id=f, id@g=g となる写像の単位元
    data = [0] * n
    return (op, op_e, mapping, composition, comp_e, n, data)

### 使用例 ###
size = 6
lst = LazySegmentTree(*seg_func(size))  # 区間の長さが5の遅延セグメント木を作成

def g(x,a):
    if x<=a:
        return (True)
    else:
        return (False)


size = 5
lazy_segtree = LazySegmentTree(*seg_func(size))  # 区間の長さが5の遅延セグメント木を作成
print("区間最大値取得, 区間加算")
lazy_segtree.apply_lr(0, 1, 5)  # 半開区間[0, 1)の値を5加算
print(lazy_segtree.prod(0, 4))  # 半開区間[0, 4)で最大値5を出力
lazy_segtree.apply_lr(0, 3, 6)  # 半開区間[0, 3) の値を6加算
print(lazy_segtree.all_prod())  # 全区間の最大値11を出力
print("\n")


# ----------------------------------------------------------------------------------------------
# 区間最小値取得、区間加算
def seg_func(n: int):
    inf = float("inf")
    def op(l: int, r: int): return min(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)
    op_e = inf  # 二項演算・の単位元
    def mapping(f: int, x: int): return f + x  # 遅延していたものを要素に反映させる関数
    def composition(f: int, g: int): return f + g  # 遅延操作を追加する関数
    comp_e = 0  # f@id=f, id@g=g となる写像の単位元
    data = [0] * n
    return (op, op_e, mapping, composition, comp_e, n, data)

### 使用例 ###
size = 5
lazy_segtree = LazySegmentTree(*seg_func(size))  # 区間の長さが5の遅延セグメント木を作成

print("区間最小値取得, 区間加算")
lazy_segtree.apply_lr(0, 4, 5)  # 半開区間[0, 4)の値を5加算
print(lazy_segtree.prod(2, 5))  # 半開区間[2, 5)で最小値0を出力
lazy_segtree.apply_lr(0, 3, -6)  # 半開区間[0, 3)の値を-6加算
print(lazy_segtree.all_prod())  # 全区間の最小値-1出力
print("\n")


# ----------------------------------------------------------------------------------------------
# 区間和取得, 区間加算
def seg_func(n: int):
    from dataclasses import dataclass
    @dataclass
    class V:
        value: int
        length: int

    def op(l: V, r: V): return V(l.value + r.value, l.length + r.length)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)
    op_e = V(0, 0)  # 二項演算・の単位元
    def mapping(f: int, x: V): return V(x.value + x.length*f, x.length)  # 遅延していたものを要素に反映させる関数
    def composition(f: int, g: int): return f + g  # 遅延操作を追加する関数
    comp_e = 0  # f@id=f, id@g=g となる写像の単位元
    data = [V(0, 1) for _ in range(n)]
    return (op, op_e, mapping, composition, comp_e, n, data)

### 使用例 ###
size = 5
lazy_segtree = LazySegmentTree(*seg_func(size))  # 区間の長さが5の遅延セグメント木を作成

print("区間和取得, 区間加算")
lazy_segtree.apply_lr(0, 3, 5)  # 半開区間[0, 3)の値を5加算
print(lazy_segtree.prod(1, size).value)  # 半開区間[1, 5)の総和10を出力
lazy_segtree.apply_lr(3, size, 6)  # 半開区間[3, 5) の値を6加算
print(lazy_segtree.all_prod().value)  # 全区間の総和27を出力
print("\n")


# ----------------------------------------------------------------------------------------------
# 区間最大値取得、区間更新
def seg_func(n: int):
    inf = float("inf")
    def op(l: int, r: int): return max(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)
    op_e = -inf  # 二項演算・の単位元
    def mapping(f, x: int): return x if f == comp_e else f  # 遅延していたものを要素に反映させる関数
    def composition(f, g): return g if f == comp_e else f  # 遅延操作を追加する関数
    comp_e = None  # f@id=f, id@g=g となる写像の単位元
    data = [0] * n
    return (op, op_e, mapping, composition, comp_e, n, data)

### 使用例 ###
size = 5
lazy_segtree = LazySegmentTree(*seg_func(size))  # 区間の長さが5の遅延セグメント木を作成

print("区間最大値取得, 区間更新")
lazy_segtree.apply_lr(0, 1, 5)  # 半開区間[0, 1)の値を5に更新
print(lazy_segtree.prod(0, 4))  # 半開区間[0, 4)で最大値5を出力
lazy_segtree.apply_lr(0, 3, 6)  # 半開区間[0, 3) の値を6加算
print(lazy_segtree.all_prod())  # 全区間の最大値6を出力
print("\n")


# ----------------------------------------------------------------------------------------------
# 区間最小値取得、区間更新
def seg_func(n: int):
    inf = float("inf")
    def op(l: int, r: int): return min(l, r)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)
    op_e = inf  # 二項演算・の単位元
    def mapping(f: int, x: int): return x if f == comp_e else f  # 遅延していたものを要素に反映させる関数
    def composition(f: int, g: int): return g if f == comp_e else f  # 遅延操作を追加する関数
    comp_e = None  # f@id=f, id@g=g となる写像の単位元
    data = [inf] * n
    return (op, op_e, mapping, composition, comp_e, n, data)

### 使用例 ###
size = 5
lazy_segtree = LazySegmentTree(*seg_func(size))  # 区間の長さが5の遅延セグメント木を作成

print("区間最小値取得, 区間更新")
lazy_segtree.apply_lr(0, 4, 5)  # 半開区間[0, 4)の値を5に更新
print(lazy_segtree.prod(2, size))  # 半開区間[2, 5)で最小値0を出力
lazy_segtree.apply_lr(0, 3, -6)  # 半開区間[0, 3)の値を-6に更新
print(lazy_segtree.all_prod())  # 全区間の最小値-6出力
print("\n")


# ----------------------------------------------------------------------------------------------
# 区間和取得, 区間更新
def seg_func(n: int):
    from dataclasses import dataclass
    @dataclass
    class V:
        value: int
        length: int

    def op(l: V, r: V): return V(l.value + r.value, l.length + r.length)  # 二項演算関数 (区間最大 : max, 区間和 : sum など)
    op_e = V(0, 0)  # 二項演算・の単位元
    def mapping(f, x: V):  # 遅延していたものを要素に反映させる関数
        if f != comp_e: x.value = f * x.length
        return x
    def composition(f, g): return g if f == comp_e else f  # 遅延操作を追加する関数
    comp_e = None  # f@id=f, id@g=g となる写像の単位元
    data = [V(0, 1) for _ in range(n)]  # [値, 区間の長さ]
    return (op, op_e, mapping, composition, comp_e, n, data)

### 使用例 ###
size = 5
lazy_segtree = LazySegmentTree(*seg_func(size))  # 区間の長さが5の遅延セグメント木を作成

print("区間和取得, 区間更新")
lazy_segtree.apply_lr(0, 3, 5)  # 半開区間[0, 3)の値を5加算
print(lazy_segtree.prod(1, size).value)  # 半開区間[1, 5)の総和10を出力
lazy_segtree.apply_lr(3, size, 6)  # 半開区間[3, 5) の値を6加算
print(lazy_segtree.all_prod().value)  # 全区間の総和27を出力