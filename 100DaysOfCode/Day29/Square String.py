#problem statement: https://codeforces.com/problemset/problem/1619/A

testCnt=int(input())

for _ in range(testCnt):
    inStr=input()
    strLen=len(inStr)
    if strLen%2==0:
        if inStr[:strLen//2]==inStr[strLen//2:]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")