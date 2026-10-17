from collections import defaultdict
import operator
import math, string

"""
注意1:
クエリタイプ1のr - lの総和が大きくなりすぎると，復元の都合でTLEになる．
(別のデータ構造を考えたり，このコードをいじる必要が出てくる)
文字列が与えられて，それが一致するかという判定には使えそう．

注意2:
遅延セグ木で区間更新varも考えたけれど，
文字列は一括で同じ値を更新する訳ではないので，難しそう．

注意3:
文字列の復元も考えたけれど難しい......
モジュロ演算を用いたらいけるはずだけど，長さ30程度でバグ発生したのであきらめ．

応用例：
回文判定にも使えるっぽい．
1回出てるのでもう出なさそうだけど，応用問題には使える．
"""

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


# --------------- ローリングハッシュの構築 --------------------------------------------
base = 135252661172689 # ハッシュの奇数 (代数的性質により素数のみ有効)
abc = string.ascii_lowercase
S_ls = []
f = defaultdict(int)    # 更新の際に有用．スカラー倍のスカラー部が小さくなる．
for s in range(len(abc)):
    f[abc[s]] = s

N, Q = map(int, input().split())
# --------------------------------------------------------------------------------
S = input() # ここを変更（入力部） ---------------------------------------------------
exp = 1
exp_ls = []     # 一点更新の際に必要
inv_exp_ls = [] # 一点更新の際に必要
inv_base = pow(len(abc), base - 2, base)
for i in range(len(S)):
    S_ls.append((f[S[i]] * exp) % base)
    exp_ls.append(exp)
    inv_exp_ls.append(pow(exp, base - 2, base))
    exp *= len(abc)
    exp %= base
rh = SegTree(S_ls, "add")   # セグ木の構築

# ------------------- 動作確認 ----------------------------------------
"""
クエリタイプ1 : 
    S[l, r] の文字列のハッシュ値が返される．
    入力format : t, l, r

クエリタイプ2 : 
Sのi文字目をcに変更．
    入力format : t, i, c
"""
for _ in range(Q):
    q = list(input().split())
    if q[0] == "1":
        l = int(q[1]) - 1
        r = int(q[2])
        s = rh.query(l, r) * inv_exp_ls[l] % base
        print(s)
    else:
        i = int(q[1]) - 1
        rh.update(i, (exp_ls[i] * f[q[2]]) % base)
