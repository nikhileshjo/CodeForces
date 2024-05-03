#problem statement: https://codeforces.com/problemset/problem/1873/B

testCnt=int(input())

for _ in range(testCnt):
    arrLen=input()
    arr=list(map(int,input().split()))
    arr.sort()
    arr[0]+=1
    res=1
    for i in arr:
        res*=i
    print(res)