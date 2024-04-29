#problem statement: https://codeforces.com/problemset/problem/1829/A

testCnt=int(input())

for _ in range(testCnt):
    result=0
    for i,j in zip(input(),'codeforces'):
        if i!=j:
            result+=1
    print(result)