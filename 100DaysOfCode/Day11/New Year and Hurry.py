#problem statement: https://codeforces.com/problemset/problem/750/A

problemCnt,travelTime = map(int,input().split())
timeConsm=travelTime
i=0
for i in range(1,problemCnt+1):
    if timeConsm+(5*i)>240:
        i-=1
        break
    else:
        timeConsm+=(5*i)
if i>problemCnt:
    print(problemCnt)
else:
    print(i)