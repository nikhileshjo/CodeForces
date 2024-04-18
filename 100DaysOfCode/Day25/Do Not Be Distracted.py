#problem statement: https://codeforces.com/problemset/problem/1520/A

testCnt=int(input())
for _ in range(testCnt):
    workDays=input()
    workLog=input()
    prev=workLog[0]
    workDone=[]
    flag=False
    for i in workLog:
        if i!=prev:
            workDone.append(prev)
            prev=i
        if i in workDone:
            print("NO")
            flag=True
            break
    if not flag:
        print("YES")
