#problem statement: https://codeforces.com/problemset/problem/1760/A

testCnt=int(input())
for _ in range(testCnt):
    nums=list(map(int,input().split()))
    nums.sort()
    print(nums[1])