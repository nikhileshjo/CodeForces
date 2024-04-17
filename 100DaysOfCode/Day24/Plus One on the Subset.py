#problem statment: https://codeforces.com/problemset/problem/1624/A

testCnt=int(input())

for _ in range(testCnt):
    arrLen=input()
    arr=tuple(map(int,input().split()))
    print(max(arr)-min(arr))