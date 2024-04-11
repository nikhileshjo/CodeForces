#problem statement: https://codeforces.com/problemset/problem/1512/A

testCnt=int(input())
for _ in range(testCnt):
    numLen=input()
    numList=list(input().split())
    numSet=set(numList)
    for num in numSet:
        eleCnt=numList.count(num)
        if eleCnt==1:
            print(numList.index(num)+1)