from collections import defaultdict

l=defaultdict(list)
#dを初期化しなくても，参照したときにd(class:dict)を初期化してくれる．
l[0].append(1)
l[2].append(10)

print(l[0])
print(l[1])
print(l)

#defaultdict(データの型)，データの型はset，list，tuple,intなどなんでもできる．
s=defaultdict(set)
s[2]|={2}
print(s)

#Z^2→string の写像もできる．
d=defaultdict(tuple)
d[(1,2)]="a"
print(d)