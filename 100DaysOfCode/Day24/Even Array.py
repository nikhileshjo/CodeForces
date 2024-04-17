#problem statement: https://codeforces.com/problemset/problem/1367/B

testCnt=int(input())
for _ in range(testCnt):
    arrLen=int(input())
    arr=tuple(map(int,input().split()))
    oddWrong=[]
    evenWrong=[]

    for i in range(arrLen):
        if i%2==0:
            if arr[i]%2!=0:
                oddWrong.append(arr[i])
        else:
            if arr[i]%2==0:
                evenWrong.append(arr[i])
    oddLen=len(oddWrong)
    evenLen=len(evenWrong)
    if oddLen==evenLen:
        print(oddLen)
    else:
        print(-1)