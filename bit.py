print(7&1)
print(1^3)


# 上の方が速いけど考えやすいのは下
def bit_and(S1 : str, S2 : str):
    """
    S1,S2:0,1のstring → ANDをとった文字列

    コスト:O(max(len(S1), len(S2)))
    """

    ret = []

    # 桁数を合わせてるだけ．
    zero = "0" * abs(len(S1) - len(S2))
    if len(S1) > len(S2):
        S2 = zero + S2
    else:
        S1 = zero + S1


    for i in range(max(len(S1), len(S2))):
        if S1[i] == S2[i] == "1":
            ret.append("1")
        else:
            ret.append("0")

    return "".join(ret)


def bit_or(S1 : str, S2 : str):
    """
    S1,S2:0,1のstring → ORをとった文字列

    コスト:O(max(len(S1), len(S2)))
    """
    ret = []

    # 桁数を合わせてるだけ．
    zero = "0" * abs(len(S1) - len(S2))
    if len(S1) > len(S2):
        S2 = zero + S2
    else:
        S1 = zero + S1


    for i in range(max(len(S1), len(S2))):
        if S1[i] == "1" or S2[i] == "1":
            ret.append("1")
        else:
            ret.append("0")

    return "".join(ret)

def bit_xor(S1 : str, S2 : str):
    """
    S1,S2:0,1のstring → XORをとった文字列

    コスト:O(max(len(S1), len(S2)))
    """
    ret = []

    # 桁数を合わせてるだけ．
    zero = "0" * abs(len(S1) - len(S2))
    if len(S1) > len(S2):
        S2 = zero + S2
    else:
        S1 = zero + S1


    for i in range(max(len(S1), len(S2))):
        if S1[i] != S2[i]:
            ret.append("1")
        else:
            ret.append("0")

    return "".join(ret)

def bit_not(S):
    """
    S:0,1のstring → NOTをとった文字列

    コスト:O(max(len(S)))
    """

    ret = []

    for i in range(len(S)):
        if S[i] != "1":
            ret.append("1")
        else:
            ret.append("0")

    return "".join(ret)

# int を bit に変換．
def Num_shift(n):
    # int → bit
    ret = ""
    while True:
        if n == 0:
            return ret
        ret = str(n % 2) + ret
        n //= 2

# bit を int に変換．
def Bit_shift(b):
    # bit → int
    ret = 0
    for i in range(len(b)):
        ret += int(b[i]) * (2 ** (len(b) - i - 1))
    return ret

# 使用例１
print(bit_and("10101","0110"))
print(bit_or("10101","0110"))
print(bit_xor("10101","0110"))
print(bit_not("101"))

# 使用例２
# 一文字ずつ見ていく方法．全ての命題で可能．
# 今回は ￢bit1 ∨ bit2 を確認．
bit1 = "10101001"
bit2 = "1110"

zero = "0" * abs(len(bit1) - len(bit2))
if len(bit1) > len(bit2):
    bit2 = zero + bit2
else:
    bit1 = zero + bit1

ans = ""
for i in range(max(len(bit1), len(bit2))):
    ans += bit_or(bit_not(bit1[i]), bit2[i])

print(ans)

# 63bit以下の整数を2進数表記したときに立っているbit数
def popcount64(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x7f

# 多分，こっちを使う方が楽そう．
# bit_count() : 2進数表記で1の数を数える
x, y, z = 13, 30, 255
print(x.bit_count())  # 3 (13の2進数表記は1101)
print(y.bit_count())  # 4 (30の2進数表記は11110)
print(z.bit_count())  # 8 (255の2進数表記は11111111)