#problem statment: https://codeforces.com/problemset/problem/1542/A

for _ in range(int(input())):
    n=input()
    arr=tuple(map(int,input().split()))
    oddCnt=len([num for num in arr if num%2!=0])
    evenCnt=len([num for num in arr if num%2==0])
    if evenCnt==oddCnt:
        print("YES")
    else:
        print("NO")
