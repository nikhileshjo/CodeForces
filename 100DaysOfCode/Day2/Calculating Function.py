#problem statement: https://codeforces.com/problemset/problem/486/A

n=int(input())
if n%2==0:
    print(int(n/2))
else:
    print(int(-(n+1)/2))