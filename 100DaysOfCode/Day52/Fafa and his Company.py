#problem statement: https://codeforces.com/problemset/problem/935/A

num=int(input())
res=0
for i in range(1,(num//2)+1):
    if (num-i)%i==0:
        res+=1
print(res)