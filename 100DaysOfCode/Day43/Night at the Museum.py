#problem statement: https://codeforces.com/problemset/problem/731/A

inStr=input()
alpha=tuple(chr(i) for i in range(ord('a'), ord('z')+1))
pos=0
res=0
for i in inStr:
    newPos=alpha.index(i)
    diff=abs(newPos-pos)
    if diff<=13:
        res+=diff
    else:
        res+=26-diff
    pos=newPos
print(res)