#link to question: https://codeforces.com/problemset/problem/469/A
TotalLevels=int(input())
xLevels=list(map(int,input().split()))
yLevels=list(map(int,input().split()))

for i in range(1,TotalLevels+1):
    if i not in xLevels[1:] and i not in yLevels[1:]:
        print("Oh, my keyboard!")
        exit()
    else:
        pass
print("I become the guy.")