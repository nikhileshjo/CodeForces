#problem statement: https://codeforces.com/problemset/problem/758/A

citizenCnt=input()

wages=list(map(int,input().split()))

maxWage=max(wages)
expense=0
for i in wages:
    expense+=(maxWage-i)
print(expense)