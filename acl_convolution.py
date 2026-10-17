from atcoder.convolution import convolution


"""
aは，x + 2 x ^ 2 + 3 x ^ 3 の x ^ i の係数，
bは，x + 4 x ^ 2 の x ^ i の係数
を表す．
"""
a = [1, 2, 3]
b = [1, 4]

c = convolution(998244353, a, b)
"""
cは，(x + 2 x ^ 2 + 3 x ^ 3) (x + 4 x ^ 2) の　x ^ i の係数を表す．

コスト：O(N logN)
メモ　：
    FFT はまだ理解してない．（授業でやったけど）
    形式的べき級数(FPS)でよく使いそう．
"""
print(c)  # 出力: [1, 3, 5, 3]
