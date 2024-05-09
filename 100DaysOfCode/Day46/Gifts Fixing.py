#problem statement: https://codeforces.com/problemset/problem/1399/B

for _ in range(int(input())):
    arrLen=input()
    canArr=tuple(map(int,input().split()))
    orgArr=tuple(map(int,input().split()))
    canMin=min(canArr)
    orgMin=min(orgArr)
    result=0
    for can,org in zip(canArr,orgArr):
        canDiff=can-canMin
        orgDiff=org-orgMin
        result+=min(canDiff,orgDiff)+abs(canDiff-orgDiff)
    print(result)