import operator
import math
# operator は，数学の演算子に対応するものという認識．
# セグ木，写経


class SegTree:
    """
    データ構造の作成    : O(NlogN)
    データの更新       : O(logN)
    データの取得       : O(1)

    できること
    ・データの一点更新
    ・データの区間取得
    """

    # デフォルトは最小値
    def __init__(self, init_val, type = 'min', ide_ele = None):
        # 演算子の定義

        settings = {
            'min': (min, float('inf')),     # 最小値
            'max': (max, -float("inf")),    # 最大値
            'add': (operator.add, 0),       # 加算
            'mul': (operator.mul, 1),       # 乗算
            'gcd': (math.gcd, 0),           # 最大公約数
            'lcm': (lambda x, y: (x * y) // math.gcd(x, y), 1), # 最小公倍数
            'or': (operator.or_, 0),        # 論理和 or
            'and': (operator.and_, 1),      # 論理積 and
            'xor': (operator.xor, 0)        # 排他的論理和 xor 　，排他的論理的 xandとする場合は，not xor とすればよい．
        }

        n = len(init_val)

        # 例外(エラー)処理，https://note.nkmk.me/python-try-except-else-finally/
        try:
            if ide_ele is None:
                self.segfunc, self.ide_ele = settings[type]
            else:
                self.segfunc, self.ide_ele = settings[type][0], ide_ele
        except:
            exit(f'type として未定義の {type} が指定されています．')

        self.num = 1 << (n - 1).bit_length()    # 葉の数．完全2分木の葉に元のデータを入れるので，2の累乗個．
        # bit_length : 整数を，符号と先頭の 0 は除いて二進法で表すために必要なビットの数を返します． https://docs.python.org/ja/3/library/stdtypes.html
        self.tree = [self.ide_ele] * (2 * self.num)   # セルの作成．葉の数×2-1個存在．1-index
        # 初期値の設定，0-index -> 1-index
        for i in range(n):
            self.tree[self.num + i] = init_val[i]

        for i in range(self.num - 1, 0, -1):
            # 葉以外のセルの設定．1-index．根のindexが1．
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])



    def update(self, k, x):
        # k番目(0-index)の値を x に更新

        k += self.num       # 葉の位置．0-index -> 1-index
        self.tree[k] = x    # 葉の値の更新
        # 葉以外の変更すべきセルの値を更新．葉の方(根から遠いところ)から，更新してる．
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1


    def add(self, k, x):
        # k番目(0-index)の値に x を加算．
        self.update(k, self.val(k) + x)

    def mul(self, k, x):
        # k番目(0-index)の値に x を乗算．
        self.update(k, x * self.val(k))


    def query(self, l, r):
        # 半開区間 [l,r) に対するクエリ． l,r : 0-index

        res = self.ide_ele
        # 葉の位置． 0-index -> 1-index
        l += self.num
        r += self.num

        # ここの操作がよくわからん泣．主に if文による条件分岐のところ．
        while l < r:
            if l & 1:       # l が奇数(右側のセル)のとき
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:       # rが奇数（右側のセル）のとき．右側は閉区間なので含まず，その左のセルまでが対象
                res = self.segfunc(res, self.tree[r-1])

            # 親のセルへ
            l >>= 1
            r >>= 1
        return res


    def val(self, k):
        # 葉の値を返す．
        return self.tree[k + self.num]

# 使用例 1
print("ex1")
a = [3, 5, 9, 13, 7, 12, 11, 2, 7, 8]   # 初期リスト
seg = SegTree(a, 'min')                 # インスタンスの作成．デフォルトの最小値'min'は省略可
print(seg.val(1))                       # a[1]を表示 --> 5
print(seg.query(1, 7))                  # a[1]～a[6]の最小値を表示 --> 5
print(seg.query(0, 10))                 # a[0]～a[9]の最小値を表示 --> 2. a[10]は存在しない
seg.update(5, 1)                        # a[5]を1に変更
print(seg.query(1, 7))                  # a[1]～a[6]の最小値を表示 --> 1
seg.add(5, 2)                           # a[5]に2を追加して 3になる
print(seg.query(1, 7))                  # a[1]～a[6]の最小値を表示 --> 3

print()
# 使用例 2
print("ex2")
# セグメント木の作成
seg_cnt = SegTree([0] * (11), type='add')   # [0, 10]におけるデータの個数
seg_sum = SegTree([0] * (11), type='add')   # [0, 10]におけるデータの値の総和

seg_cnt.add(5, 1)   			# 個数用に 5を1つ追加
seg_sum.add(5, 5)   			# 合計用にも 5を1つ追加
print(seg_cnt.query(0, 5))      # 区間[0, 5) = [0, 4]にはデータなし  --> 0
print(seg_cnt.query(5, 6))      # 区間[5, 6) = [5, 5]にデータは1件   --> 1
seg_cnt.add(5, 1)   			# 個数用に 5を1つ追加
seg_sum.add(5, 5)   			# 合計用にも 5を1つ追加
seg_cnt.add(2, 1)   			# 個数用に 2を1つ追加
seg_sum.add(2, 2)   			# 合計用にも 2を1つ追加
print(seg_cnt.query(0, 5))      # 区間[0, 5) = [0, 4]にはデータは1件    --> 1
print(seg_cnt.query(5, 6))      # 区間[5, 6) = [5, 5]にデータは2件      --> 2
print(seg_sum.query(0, 5))      # 区間[0, 4]内のデータは 2のみ．合計2      --> 2
print(seg_sum.query(2, 8))      # 区間[2, 7]内のデータは {2, 5, 5}．合計12  --> 12