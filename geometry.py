# 参考：https://qiita.com/zu_rin/items/e04fdec4e3dec6072104
# 引用：https://tjkendev.github.io/procon-library/python/geometry/segment_line_intersection.html


# 線分同士の交点判定
def dot3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)
def cross3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)
def dist2(A, B):
    ax, ay = A; bx, by = B
    return (ax - bx) ** 2 + (ay - by) ** 2
def is_intersection(P0, P1, Q0, Q1):
    C0 = cross3(P0, P1, Q0)
    C1 = cross3(P0, P1, Q1)
    D0 = cross3(Q0, Q1, P0)
    D1 = cross3(Q0, Q1, P1)
    if C0 == C1 == 0:
        E0 = dot3(P0, P1, Q0)
        E1 = dot3(P0, P1, Q1)
        if not E0 < E1:
            E0, E1 = E1, E0
        return E0 <= dist2(P0, P1) and 0 <= E1
    return C0 * C1 <= 0 and D0 * D1 <= 0

# 線分と線分
print(is_intersection((0, 0), (1, 1), (0, 1), (1, 0)))
# => "True"
print(is_intersection((0, 0), (1, 1), (0, 2), (3, 2)))
# => "False"

# 点と線分の交差判定: 点 (1, 1)
print(is_intersection((1, 1), (1, 1), (0, 0), (3, 3)))
# => "True"
print(is_intersection((1, 1), (1, 1), (-3, -2), (1, 1)))
# => "True"


import math


def Euclid_Dist(x: list, y: list):
    """
    ・:input
        x, y : 同じ長さのlist
    ・:return
        x, y のユークリッド距離
    ・:コスト
        O(len(x))
    """

    ret = 0
    for i in range(len(x)):
        ret += (x[i] - y[i]) ** 2
    return math.sqrt(ret)