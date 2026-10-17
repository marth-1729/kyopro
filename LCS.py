def LCS(A : list, B : list):
    """
    A, B : list -> C : list
    2つのlist A, Bを入れると，2つの共通部分列のうち，最長となる list を返す関数．
    コスト : O(len(A) * len(B))
    """
    dp = [(10 ** 10, [])]  * (len(B) + 1)
    dp[0] = (- 1, [])
    tmp = [(10 ** 10, [])] * (len(B) + 1)
    tmp[0] = (- 1, [])
    for i in range(len(A)):
        j = 0
        k = 0
        while True:
            if k == len(dp):
                break
            while j < len(B) and k < len(dp):
                if dp[k][0] < j and A[i] == B[j]:
                    if dp[k + 1][0] >= j:
                        tmp[k + 1] = (j, dp[k][1] + [B[j]])
                    break
                j += 1
            k += 1
        for i in range(len(dp)):
            dp[i] = tmp[i]

    ans = []
    for i, j in dp:
        if j != []:
            ans = j
    return ans

# 作成者 : marth_1729 (まーす)
# AC : https://atcoder.jp/contests/dp/tasks/dp_f
# 上のlist 版を作成．
s = input()
t = input()
S = []
T = []
for ss in s:
    S.append(ss)
for tt in t:
    T.append(tt)

print("".join(LCS(S, T)))