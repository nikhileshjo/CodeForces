#problem statement: https://codeforces.com/problemset/problem/510/A
rowCnt,colCnt=map(int,input().split())
flag=1
for i in range(1,rowCnt+1):
    if i%2==0:
        if flag:
            print(("."*(colCnt-1))+"#")
            flag=0
        else:
            print("#"+("."*(colCnt-1)))
            flag=1
    else:
        print("#"*colCnt)