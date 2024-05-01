#problem statement: https://codeforces.com/problemset/problem/1371/A

testCnt=int(input())

for _ in range(testCnt):
    n=int(input())
    if n%2==0:
        print(n//2)
    else:
        print((n//2)+1)