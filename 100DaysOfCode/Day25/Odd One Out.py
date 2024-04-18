#problem statement: https://codeforces.com/problemset/problem/1915/A

testCnt=int(input())
for _ in range(testCnt):
    a,b,c=map(int,input().split())
    diff1=a-b
    diff2=b-c
    if diff1==0 and diff2!=0:
        print(c)
    elif diff1!=0 and diff2==0:
        print(a)
    else:
        print(b)