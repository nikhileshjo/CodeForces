#problem statement: https://codeforces.com/problemset/problem/443/A

alphSet=set(input()[1:-1].split(", "))
if '' not in alphSet:
    print(len(alphSet))
else:
    print(0)