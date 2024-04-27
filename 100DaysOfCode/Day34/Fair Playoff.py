#problem statement: https://codeforces.com/problemset/problem/1535/A

testCnt=int(input())
for _ in range(testCnt):
    skills=list(map(int,input().split()))
    topTwo=sorted(skills)[2:]
    if topTwo==sorted(skills[:2]) or topTwo==sorted(skills[2:]):
        print("NO")
    else:
        print("YES")