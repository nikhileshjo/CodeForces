#problem statement: https://codeforces.com/problemset/problem/1426/A

testCnt=int(input())

for _ in range(testCnt):
    appNo,appCnt=map(int,input().split())
    if appNo<=2:
        print(1)
    else:
        i=2+appCnt
        floorNo=2
        while i<appNo:
            i+=appCnt
            floorNo+=1
        print(floorNo)