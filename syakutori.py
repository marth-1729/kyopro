#尺取り法
#例　ABC143 C問題

N=int(input())
S=input()

r=1
l=0
ans=S[0]
while True:
    while True:
        if r==N:
            break
        if S[l]==S[r]:
            r+=1
            continue
        else:
            break
    if r==N:
        break
    ans+=S[r]
    l=r
print(ans)
print(len(ans))