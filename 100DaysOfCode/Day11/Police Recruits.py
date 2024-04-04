# problem statement: https://codeforces.com/problemset/problem/427/A

inCnt=input()
crimePol=list(map(int,input().split()))

polAvail=0
crimeCnt=0

for i in crimePol:
    if i==-1:
        if i+polAvail<0:
            crimeCnt+=1
        else:
            polAvail-=1
    else:
        polAvail+=i

print(crimeCnt)