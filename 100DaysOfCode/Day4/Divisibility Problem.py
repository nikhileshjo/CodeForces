#problem statement: https://codeforces.com/problemset/problem/1328/A
testCaseCnt=int(input())
output=[]
for _ in range(testCaseCnt):
    a,b=map(int,input().split())
    if a%b==0:
        result=0
    else:
        result=b-(a%b)
    output.append(result)
for i in output:
    print(i)