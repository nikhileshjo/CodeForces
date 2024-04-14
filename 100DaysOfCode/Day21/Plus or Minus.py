#problem statement: https://codeforces.com/problemset/problem/1807/A

testCnt=int(input())

for _ in range(testCnt):
    a,b,c=map(int,input().split())
    if a+b==c:
        print("+")
    else:
        print("-")