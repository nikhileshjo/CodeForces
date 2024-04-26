#problem statement: https://codeforces.com/problemset/problem/707/A

n,m=map(int,input().split())
color=False
photo=[]
for n in range(n):
    photo.append(input())
for colours in photo:
    if ("C" in colours) or ("M" in colours) or ("Y" in colours):
        print("#Color")
        color=True
        break
if not color:
    print("#Black&White")