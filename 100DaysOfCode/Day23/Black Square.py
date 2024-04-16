#problem statement: https://codeforces.com/problemset/problem/431/A

sqCal=list(map(int,input().split()))
totalCal=0
blackSq=input()
for i in blackSq:
    if i == '1':
        totalCal+=sqCal[0]
    elif i == '2':
        totalCal+=sqCal[1]
    elif i == '3':
        totalCal+=sqCal[2]
    else:
        totalCal+=sqCal[3]
print(totalCal)