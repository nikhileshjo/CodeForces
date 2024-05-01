#problem statement: https://codeforces.com/problemset/problem/1742/B

testCnt=int(input())

for _ in range(testCnt):
    listCnt=int(input())
    inList=set(input().split())
    if len(inList)==listCnt:
        print("YES")
    else:
        print("NO")