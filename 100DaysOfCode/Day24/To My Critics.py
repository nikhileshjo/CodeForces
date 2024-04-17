#problem statement: https://codeforces.com/problemset/problem/1850/A

testCnt=int(input())

for i in range(testCnt):
    nums=list(map(int,input().split()))
    nums.sort()
    if nums[1]+nums[2]>=10:
        print("YES")
    else:
        print("NO")