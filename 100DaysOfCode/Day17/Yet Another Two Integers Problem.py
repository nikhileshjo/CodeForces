#problem statement: https://codeforces.com/problemset/problem/1409/A

testCaseCnt=int(input())

for _ in range(testCaseCnt):
    a,b=map(int,input().split())
    if b>a:
        if b-a<10:
            print(1)
        else:
            res=(b-a)//10
            if (res*10+a)!=b:
                print(res+1)
            else:
                print(res)
    elif b<a:
        if a-b<10:
            print(1)
        else:
            res=(a-b)//10
            if (a-res*10)!=b:
                print(res+1)
            else:
                print(res)
    else:
        print(0)