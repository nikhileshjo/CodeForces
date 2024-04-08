# problem statement: https://codeforces.com/problemset/problem/1742/A

testCaseCnt=int(input())

for _ in range(testCaseCnt):
    numList=list(map(int,input().split()))
    numList.sort(reverse=True)
    if numList[0]==numList[1]+numList[2]:
        print("YES")
    else:
        print("NO")