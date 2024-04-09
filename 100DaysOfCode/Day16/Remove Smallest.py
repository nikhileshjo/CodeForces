#problem statement: https://codeforces.com/problemset/problem/1399/A

testCaseCnt=int(input())
for _ in range(testCaseCnt):
    flag=1
    numListCnt=int(input())
    if numListCnt==1:
        numList=input()
        print("YES")
    else:
        numList=list(map(int,input().split()))
        numList.sort(reverse=True)
        for i in range(numListCnt-1):
            if numList[i]-numList[i+1]>1:
                print("NO")
                flag=0
                break
        if flag==1:
            print("YES")
    