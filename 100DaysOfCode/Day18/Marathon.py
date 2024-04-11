#problem statement: https://codeforces.com/problemset/problem/1692/A

testCnt=int(input())

for _ in range(testCnt):
    dists=list(map(int,input().split()))
    res=0
    for dist in dists[1:]:
        if dist>dists[0]:
            res+=1
    print(res)