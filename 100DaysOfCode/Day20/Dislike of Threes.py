#problem statement: https://codeforces.com/problemset/problem/1560/A

testCnt=int(input())
nums=[]
for _ in range(testCnt):
    nums.append(int(input()))

favList=[]
j=1
for _ in range(1,max(nums)+1):
    while j%3==0 or j%10==3:
        j+=1
    favList.append(j)
    j+=1

for i in nums:
    print(favList[i-1])