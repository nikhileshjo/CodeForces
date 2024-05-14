#problem statment: https://codeforces.com/problemset/problem/702/A

arrLen=int(input())
arr=tuple(map(int,input().split()))
tmp=1
res=1
prv=arr[0]
cnt=0
for i in arr:
    cnt+=1
    if cnt==1:
        continue
    if i>prv:
        tmp+=1
    else:
        if res<tmp:
            res=tmp
        tmp=1
    prv=i
if res<tmp:
        res=tmp
print(res)