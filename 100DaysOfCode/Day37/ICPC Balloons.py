#problem statement: https://codeforces.com/problemset/problem/1703/B

testCnt=int(input())

for _ in range(testCnt):
    prbCnt=input()
    prb=input()
    prbDist=set(prb)
    res=0
    for p in prbDist:
        res+=prb.count(p)+1
    print(res)