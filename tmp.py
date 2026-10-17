from collections import defaultdict
import math


# 拡張ユークリッドの互除法
# ax + by = 1 の特殊解（1つの解）を返す．a, b: 正の整数で，互いに素
def ex_euclid(a, b):
    c, d, e, f = 1, 0, 0, 1
    while b != 0:
        c, d = d, c - a // b * d
        e, f = f, e - a // b * f
        a, b = b, a % b
    return c, e


def indet_liner_eq(a, b, c):
    def sub(a, b, c):  # a, b, c: 非負整数
        if a == 0:  # a=0の処理
            if b == 0:
                return (0, 0) if c == 0 else None
            else:
                return (0, c // b) if c % b == 0 else None
        if b == 0:  # b=0の処理
            return (c // a, 0) if c % a == 0 else None
        if c == 0:  # a=0の処理
            return 0, 0

        # a, b, c: 正の整数
        g = math.gcd(a, b)
        if c % g > 0:
            return None
        aa, bb, cc = a // g, b // g, c // g  # a, b: 互いに素
        x, y = ex_euclid(aa, bb)  # aax + bby = 1 の特殊解
        return x * cc, y * cc


while True:
    M, A = map(int, input().split())
    if M == 0:
        break
    d = math.gcd(M, A)
    M_pls = set()
    MM = M
    for i in range(2, 10 ** 6 + 1):
        if MM % i == 0:
            M_pls.add(i)
            while MM % i == 0:
                MM //= i

    MM = M // d
    AA = A // d
    x, y = ex_euclid(MM, AA)
    if x > 0:
        x %= AA
    while x < 0:
        x += AA

    M_pls = list(M_pls)
    ans = - (M - x) // d
    ans *= -1
    print(ans, x)
    max_cnt = 2 ** len(M_pls)
    for i in range(1, max_cnt):
        tmp = i
        cur = 0
        cnt = 0
        a = 1
        while tmp > 0:
            if tmp % 2 == 1:
                a *= M_pls[cur]
                cnt += 1
            cur += 1
            tmp //= 2

        xx, yy = indet_liner_eq(MM, -a, x)
        if x > 0:
            xx %= AA
        while x < 0:
            xx += AA
        
        ans -= ((-1) ** (cnt % 2)) * (M // a)
    print(ans)



# 使用例
print(f'3x + 5y = 1 の特殊解は(x, y) = {ex_euclid(3, 5)}')  		# 3x2 + 5x(-1) = 1
print(f'90x + 37y = 1 の特殊解は(x, y) = {ex_euclid(90, 37)}')  	# 90x7 + 37x(-17) = 1

n=1.5
print(870*n,260*n)


while True:
    S = input()
    if S == "#":
        break
    bracket_ls = []
    c = S[0]
    cnt = 0
    ind = 0
    while ind < len(S):
        if S[ind] != c:
            bracket_ls.append((c, cnt))
            c = S[ind]
            cnt = 0
        else:
            cnt += 1
            ind += 1
    bracket_ls.append((c, cnt))
    ans = 0
    l, r = 0, 0
    r_range_upper = 0
    for c, cnt in bracket_ls:
        if c == "(":
            l += cnt
            r_range_upper += 2 * cnt
        else:
            r += cnt
            if r > 2 * l:
                r -= 2 * l
                l = 0
                # ans += (r - 2 * l + 1) // 2
                # l, r, r_range_upper = 0, 0, 0
            elif 2 * l >= r >= l:
                l, r, r_range_upper = 0, 0, 0
            elif 2 * r >= l > r:
                r -= l
                l = 0
            # elif l < r <= 2 * l:
            #     continue
            else:
                l -= 2 * r
                r = 0
                # ans += (l - 2 * r + 1) // 2
                # l, r, r_range_upper = 0, 0, 0
                # continue
                # l, r, r_range_upper = 0, 0, 0
        print(l,r)
    # print(ans + (l + 1) // 2)
    print(l,r)

n = 0.7
print(19.20 * n, 1000 * n)
# topo_sort()
from collections import deque
import sys

sys.setrecursionlimit(100000000)


def topo_sort(cnt: list):
    # cnt : もとのDAGの入次数．
    ls = deque([])
    for i in cnt:
        if cnt[i] == 0:
            ls.append(i)
    if len(ls) == 0:
        print("Error")
        exit()

    while ls:

