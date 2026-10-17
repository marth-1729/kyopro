
# 区間スケジュール問題
# 参考：https://qiita.com/syoshi_dev/items/0dbd7ec962186c005c08#%E5%8C%BA%E9%96%93%E3%82%B9%E3%82%B1%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0%E5%95%8F%E9%A1%8C%E3%82%92%E8%A6%8B%E5%88%86%E3%81%91%E3%82%8B%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88
#      https://atcoder.jp/contests/abc463/editorial/21942
# 貪欲に追加していくだけだから理解は簡単．
def interval_schedule_prob(ls):
    """
    lsは， R昇順となるような，(R_i, L_i)のlist
    """
    cnt = 0
    cur = 0
    for r, l in ls:
        if l >= cur:
            cnt += 1
            cur = r
    return cnt


# 使用例1：https://atcoder.jp/contests/abc463/tasks/abc463_d
# 一部問題の性質により変更している．
def interval_schedule_prob(ls, X):
    cnt = 0
    cur = 0
    for r, l in ls:
        # ここにεの任意性使ってる．
        if l >= cur:
            cnt += 1
            cur = r + X
    return cnt

def bisect_solution(left, right):
    global flag
    if left == right:
        if flag:
            print(-1)
        else:
            print(left)
        exit()
    X = (left + right + 1) // 2
    cnt = interval_schedule_prob(RL, X)
    if K <= cnt:
        flag = False
        bisect_solution(X, right)
    else:
        bisect_solution(left, X - 1)

N, K = map(int, input().split())
RL = []
for _ in range(N):
    L, R = map(int, input().split())
    RL.append((R, L))

flag = True
RL.sort()
print(bisect_solution(0, 10 ** 9))
