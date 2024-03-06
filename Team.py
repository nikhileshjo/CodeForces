n=int(input())
result=0
for i in range(n):
    q=list(map(int,input().split()))
    if sum(q)>=2:
        result+=1
print(result)