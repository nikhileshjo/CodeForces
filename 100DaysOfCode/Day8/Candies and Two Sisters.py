#link to problem statement: https://codeforces.com/problemset/problem/1335/A
inputCnt=int(input())
output=[]
for _ in range(inputCnt):
    candyCnt=int(input())
    if candyCnt%2==0:
        a=(candyCnt/2)+1
    else:
        a=(candyCnt//2)+1
    if candyCnt-a==0:
        output.append(0)
    else:
        output.append(int(candyCnt-a))

for i in output:
    print(i)