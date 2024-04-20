#problem statement: https://codeforces.com/problemset/problem/1873/A

testCnt=int(input())

for _ in range(testCnt):
    inStr=input()
    if inStr[0]=='a' or inStr[1]=='b' or inStr[2]=='c':
        print("YES")
    else:
        print("NO")