#problem statement: https://codeforces.com/problemset/problem/1374/A

testCnt=int(input())
for _ in range(testCnt):
    x,y,n=map(int,input().split())
    k=n
    modu=k%x
    if modu!=y:
        if modu<y:
            k=k-(modu)-(x-y)
        else:
            k=k-(modu-y)
    print(k)