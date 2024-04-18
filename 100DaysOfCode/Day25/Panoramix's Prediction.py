#problem statement: https://codeforces.com/problemset/problem/80/A

def prime_check(num):
    for i in range(2,(num//2)+1):
        if num%i==0:
            return False        
    return True

n,m=map(int,input().split())
nextPrime=None
for i in range(n+1,m+1):
    if prime_check(i):
        nextPrime=i
        break
if nextPrime==m:
    print("YES")
else:
    print("NO")