"""
n, k ≤ 10 ** 6 程度の場合の組み合わせ nCk (mod 998244353)
前処理     ：O(k)
クエリ処理 ：O(1)
"""

# スクラップボックス引用
M = 10000  # n! を求める最大の n
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


print(scr_comb(10, 2))  # 10_C_2 = 45



# スクラップボックスの改造版(普段使いはこっちの方が良さげ)
def comb(n, k, MOD):
    # n!, 1/n, 1/n! をO(n)で計算
    fact = [1] * (n + 1)  # fact[n] = (n! mod MOD)
    factinv = [1] * (n + 1)  # factinv[n] = (mod MOD における n!の逆元)
    inv = [0] * (n + 1)  # inv[n] = (mod MOD における nの逆元)
    inv[1] = 1

    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        factinv[i] = factinv[i - 1] * inv[i] % MOD


    return fact[n] * factinv[k] * factinv[n - k] % MOD

print(comb(10,2,10**9+7))


"""
n > 10 ** 6,  k ≤ 10 ** 6  程度の場合の組み合わせ nCk (mod 998244353)
前処理     ：O(1)
クエリ処理 ：O(k)
"""
# --- もしかすると，下のやつはTLE起こすかもなので，コメントアウト ---

# M = 10000  # n! を求める最大の n
# MOD = 998244353
# inv = [0] * (M + 1)  # inv[n] = (mod MOD における nの逆元)
# inv[1] = 1
# for i in range(2, M + 1):
#     inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
#
# # 後で作成
# def comb(n, k):
#     ans = 1
#     for i in range(k):
#         ans *= (n - i) * inv[i] % MOD
# -------------------------  ここまで  -------------------------

M = 10 ** 6  # n! を求める最大の n
MOD = 998244353
inv = [0] * (M + 1)  # inv[n] = (mod MOD における nの逆元)
inv[1] = 1
for i in range(2, M + 1):
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD

# これで多分大丈夫なはず．
# 後で，https://atcoder.jp/contests/abc459/tasks/abc459_e と比較してみよう．
# abc459E でAC出たので大丈夫だと思います<(_ _)>
def comb(n, k):
    ans = 1
    for i in range(k):
        ans *= (n - i) * inv[i + 1]
        ans %= MOD
    return ans
print(comb(6, 2))