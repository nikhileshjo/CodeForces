# problem statement: https://codeforces.com/problemset/problem/155/A

matches=input()
points=list(map(int,input().split()))

pMin=points[0]
pMax=points[0]
amzCnt=0
for i in points[1:]:
    if i>pMax:
        amzCnt+=1
        pMax=i
    elif i<pMin:
        amzCnt+=1
        pMin=i
    
print(amzCnt)