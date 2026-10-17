from collections import defaultdict


# 座圧1D
def compression_1d(A: list):
    f = sorted(list((set(A))))
    ret = defaultdict(int)
    for i in range(len(f)):
        ret[f[i]] = i
    ans = [-1] * N
    for i in range(N):
        ans[i] = ret[A[i]]
    return ans


N = int(input())
A = list(map(int, input().split()))
print(*compression_1d(A))


# 他作
# こっちは，座圧する前とした後の値を行き来できる．＆2次元にも拡張可能．
# ただ，まだ私は座圧ライブラリのありがたみを理解していないので，うーーんという感じ
# 引用：https://qiita.com/lowking/items/2417fd95aa3ec65e924b
class Compress:
    def __init__(self, arr):
        values = sorted(set(arr))
        self.translator = dict([(values[i], i) for i in range(len(values))])
        self.inv_translator = values

    def to_comp(self, x):
        return self.translator[x]

    def from_comp(self, v):
        return self.inv_translator[v]


class Compress2D:
    def __init__(self, arr):
        self.x = Compress([x for x, y in arr])
        self.y = Compress([y for x, y in arr])

    def to_comp(self, x):
        return (self.x.translator[x[0]], self.y.translator[x[1]])

    def from_comp(self, v):
        return (self.x.translator[v[0]], self.y.translator[v[1]])


N = int(input())
A = list(map(int, input().split()))
ans = []
a = Compress(A)
for aa in range(4):
    ans.append(a.from_comp(aa))
print(*ans)
