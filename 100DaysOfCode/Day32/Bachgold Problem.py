#problem statement: https://codeforces.com/problemset/problem/749/A

num=int(input())
if num%2==0:
    primeCnt=num//2
    output="2 "*primeCnt
else:
    num-=3
    primeCnt=num//2
    output="2 "*primeCnt+"3"
    primeCnt+=1
print(primeCnt)
print(output)