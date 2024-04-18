#problem statement: https://codeforces.com/problemset/problem/1433/A

testCnt=int(input())

for _ in range(testCnt):
    num=input()
    bottonPressed=(10*((int(num[0]))-1))
    for i in range(1,len(num)+1):
        bottonPressed+=i
    print(bottonPressed)