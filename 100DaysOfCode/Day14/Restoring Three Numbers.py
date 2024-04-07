#problem statement : https://codeforces.com/problemset/problem/1154/A

inputNums=(list(map(int,input().split())))
inputNums.sort(reverse=True)

num1=inputNums[0]-inputNums[1]
num2=inputNums[0]-inputNums[2]
num3=inputNums[0]-inputNums[3]

print(num1,num2,num3)