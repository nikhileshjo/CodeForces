#link to problem statement: https://codeforces.com/problemset/problem/268/A
teamCnt=int(input())

homeCol=[]
awayCol=[]
resCnt=0
for _ in range(teamCnt):
    a,b=input().split()
    homeCol.append(a)
    awayCol.append(b)
for i in homeCol:
    cntOcc=awayCol.count(i)
    resCnt+=cntOcc

print(resCnt)