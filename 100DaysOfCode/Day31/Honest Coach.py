#problem statement: https://codeforces.com/problemset/problem/1360/B

testCnt=int(input())

for _ in range(testCnt):
    playerCnt=int(input())
    strength=list(map(int,input().split()))
    strength.sort()
    minDiff=99999999999999
    for i in range(1,playerCnt):
        if strength[i]-strength[i-1]<minDiff:
            minDiff=strength[i]-strength[i-1]
    print(minDiff)