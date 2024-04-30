#problem statement: https://codeforces.com/problemset/problem/1676/B

testCnt=int(input())

for _ in range(testCnt):
    boxCnt=input()
    candies=list(map(int,input().split()))
    res=0
    minCandies=min(candies)
    for i in candies:
        res+=(i-minCandies)
    print(res)