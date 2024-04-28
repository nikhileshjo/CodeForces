#problem statement: https://codeforces.com/problemset/problem/1283/A

testCnt=int(input())

for _ in range(testCnt):
    hrs,mins=map(int,input().split())
    timePast=hrs*60+mins
    ans=1440-timePast
    print(ans)