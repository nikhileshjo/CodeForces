#problem statement: https://codeforces.com/problemset/problem/492/A

cubeCnt=int(input())
rowCnt=1
while True:
    cubeCnt-=(rowCnt/2)*(rowCnt+1)
    rowCnt+=1
    if cubeCnt<(rowCnt/2)*(rowCnt+1):
        rowCnt-=1
        break
print(rowCnt)