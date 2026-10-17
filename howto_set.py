# 集合A.issubset(集合B):　→ A ⊂ B であれば，True. それ以外 False

A=[]
for i in range(3):
    A.append(list(map(int,input().split())))
N=int(input())
b=[]
for i in range(N):
    b.append(int(input()))


check=set()
bingo=[{(0,0),(0,1),(0,2)},{(1,0),(1,1),(1,2)},{(2,0),(2,1),(2,2)}]
for i in b:
    for j in range(3):
        for k in range(3):
            if i==A[j][k]:
                check|={(j,k)}


if {(0,0),(0,1),(0,2)}.issubset(check):
    print("Yes")
elif {(1,0),(1,1),(1,2)}.issubset(check):
    print("Yes")
elif {(2,0),(2,1),(2,2)}.issubset(check):
    print("Yes")

elif {(0,0),(1,0),(2,0)}.issubset(check):
    print("Yes")
elif {(0,1),(1,1),(2,1)}.issubset(check):
    print("Yes")
elif {(0,2),(1,2),(2,2)}.issubset(check):
    print("Yes")

elif {(0,0),(1,1),(2,2)}.issubset(check):
    print("Yes")
elif {(2,0),(1,1),(0,2)}.issubset(check):
    print("Yes")
else:
    print("No")