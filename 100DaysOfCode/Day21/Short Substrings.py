#problem statement: https://codeforces.com/problemset/problem/1367/A

testCnt=int(input())
for _ in range(testCnt):
    rst=''
    inStr=input()
    rst+=inStr[-2]+inStr[-1]
    rst=inStr[:-2:2]+rst
    print(rst)