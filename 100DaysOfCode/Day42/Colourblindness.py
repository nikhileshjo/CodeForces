#problem statement: https://codeforces.com/problemset/problem/1722/B

testCnt=int(input())

for _ in range(testCnt):
    arrLen=int(input())
    arr1=list(input())
    arr2=list(input())

    for i in range(arrLen):
        if arr1[i]=='G':
            arr1[i]='B'
        if arr2[i]=='G':
            arr2[i]='B'
    if arr1==arr2:
        print("YES")
    else:
        print("NO")
        