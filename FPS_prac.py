# FPS の履修

# FPS の基本的な流れ．
"""
1. 問題を(次数が無限大の)多項式に置き換える．(詳しくは，下にある例を見よ)
2. 多項式をいい感じに式変形する．
3. 答えとして相応しい項の係数から答えが得られる．(詳しくは，下にある例を見よ)
"""


# 問題　：　https://atcoder.jp/contests/fps-24/tasks/fps_24_a

# この問題の方針(解説AC)
# f := (x ^ 1 + x ^ 3 + x ^ 4 + x ^ 6) と置いて，
# [x ^ N] f ^ Dを求めたらOK．
# なお，[x ^ N] f ^ D　は．多項式 f ^ D　の x ^ N の係数を表す．

"""
1. f := (x ^ 1 + x ^ 3 + x ^ 4 + x ^ 6)がこの問題の定式化．
参考　：　https://maspypy.com/%E5%A4%9A%E9%A0%85%E5%BC%8F%E3%83%BB%E5%BD%A2%E5%BC%8F%E7%9A%84%E3%81%B9%E3%81%8D%E7%B4%9A%E6%95%B0%E6%95%B0%E3%81%88%E4%B8%8A%E3%81%92%E3%81%A8%E3%81%AE%E5%AF%BE%E5%BF%9C%E4%BB%98%E3%81%91
2. f ^ D をいい感じに変形すると，
    f ^ D = (x ^ 1 + x ^ 3 + x ^ 4 + x ^ 6) ^ D
          = x ^ D (1 + x ^ 2) ^ D (1 + x ^ 3) ^ D
    が得られる．
3. (1 + x ^ 2) ^ D の各項 x ^ k (k = 0, 1, \dots, D ^ 2)の係数と
    (1 + x ^ 3) ^ D の各項 x ^ k (k = 0, 1, \dots, D ^ 3)の係数を前計算し，
    (1 + x ^ 2) ^ Dの次数と(1 + x ^ 3) ^ Dの次数の和がN - Dとなるような次数の組について
    考えてやればOK．
"""


from collections import defaultdict


M = 10 ** 6 # n! を求める最大の n
MOD = 998244353
fact = [1] * (M + 1)  # fact[n] = (n! mod MOD)
factinv = [1] * (M + 1)  # factinv[n] = (mod MOD における n!の逆元)
inv = [0] * (M + 1)  # inv[n] = (mod MOD における nの逆元)
inv[1] = 1

for i in range(2, M + 1):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    factinv[i] = factinv[i - 1] * inv[i] % MOD


def scr_comb(n, k):
    return fact[n] * factinv[k] * factinv[n - k] % MOD

comb_list1 = defaultdict(int)   # (1 + x ^ 2) ^ D の x ^ kの係数．
comb_list2 = defaultdict(int)   # (1 + x ^ 3) ^ D の x ^ kの係数．


D, N = map(int, input().split())

# 前処理
for i in range(D + 1):
    comb_list1[2 * i] = scr_comb(D, i)
    comb_list2[3 * i] = scr_comb(D, i)

ans = 0
for i in range(N - D + 1):
    ans += comb_list1[i] * comb_list2[N - D - i]
    ans %= MOD
print(ans)



# 問題　：　https://atcoder.jp/contests/fps-24/tasks/fps_24_b

# この問題の方針
# f := (1 + x) (1 + x + x ^ 2) (\sum_k x ^ {2 k}) (\sum_k x ^ {3 k}) と置いて，
# [x ^ N] fを求めたらOK．
# なお，[x ^ N] fは．多項式 fの x ^ N の係数を表す．

"""
1. f :=  (1 + x) (1 + x + x ^ 2) (sum_k x ^ {2 k}) (sum_k x ^ {3 k}) がこの問題の定式化．
参考　：　https://maspypy.com/%E5%A4%9A%E9%A0%85%E5%BC%8F%E3%83%BB%E5%BD%A2%E5%BC%8F%E7%9A%84%E3%81%B9%E3%81%8D%E7%B4%9A%E6%95%B0%E6%95%B0%E3%81%88%E4%B8%8A%E3%81%92%E3%81%A8%E3%81%AE%E5%AF%BE%E5%BF%9C%E4%BB%98%E3%81%91
2. f をいい感じに変形すると，
    f = (1 + x) (1 + x + x ^ 2) (sum_k x ^ {2 k}) (sum_k x ^ {3 k})
      = (1 + x) (1 + x + x ^ 2) / ( (1 - x ^ 2) (1 - x ^ 3))
      = 1 / (1 - x) ^ 2
      = (sum_k x ^ k ) ^ 2
    が得られる．
3. (sum_k x ^ k ) ^ 2におけるx ^ Nの係数を求めてやればOK．
"""

N = int(input())
print((N + 1) % 998244353)



# 問題　：　https://atcoder.jp/contests/fps-24/tasks/fps_24_c

# この問題の方針
# f := (\sum_{i = 0} ^ {M} x ^ i) ^ N
#    = (1 - x ^ {M + 1}) ^ {N} / (1 - x) ^ {N}
# と置く.
"""
メモ1：
1 / (1 - x) ^ {N} の部分の処理について
1 / (1 - x) = \sum_{i = 0} ^ {\infty} x ^ {i}
であるから，
1 / (1 - x)　^ {N} = ( \sum_{i = 0} ^ {\infty} x ^ {i} ) ^ {N}
となるが，このとき，1 / (1 - x)　^ {N}の x ^ {j}の係数は，重複組み合わせの考え方により，
_{N + j - 1} C_{j} となる．

メモ2：
私は，ダブリングによる解法を思いついたが，どうやらそれではTLEになるっぽい......
"""
from collections import defaultdict

# スクラップボックス引用
M = 10 ** 6  # n! を求める最大の n
MOD = 998244353

# n!, 1/n, 1/n! をO(n)で計算
fact = [1] * (M + 1)  # fact[n] = (n! mod MOD)
factinv = [1] * (M + 1)  # factinv[n] = (mod MOD における n!の逆元)
inv = [0] * (M + 1)  # inv[n] = (mod MOD における nの逆元)
inv[1] = 1

for i in range(2, M + 1):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    factinv[i] = factinv[i - 1] * inv[i] % MOD


def scr_comb(n, k):
    return fact[n] * factinv[k] * factinv[n - k] % MOD


N, M, S = map(int, input().split())
dic = defaultdict(int)
for i in range(N + 1):
    dic[i * (M + 1)] += scr_comb(N, i) * ((-1) ** (i % 2))
ans = 0
for i in range(S + 1):
    tmp = scr_comb(N + i - 1, i)
    ans += dic[S - i] * tmp
    ans %= MOD
print(ans)
