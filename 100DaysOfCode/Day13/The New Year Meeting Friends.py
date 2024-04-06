#problem statment: https://codeforces.com/problemset/problem/723/A

coordinates=list(map(int,input().split()))
minDist=max(coordinates)-min(coordinates)
print(minDist)