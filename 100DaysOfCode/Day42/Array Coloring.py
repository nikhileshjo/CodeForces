#problem statement: https://codeforces.com/problemset/problem/1857/A

testCnt=int(input())

for _ in range(testCnt):
    arrLen=input()
    arr=list(map(int,input().split()))
    if sum(arr)%2==0:
        print("YES")
    else:
        print("NO")