#problem statement: https://codeforces.com/problemset/problem/1551/A

testCnt=int(input())
for _ in range(testCnt):
    inNum=int(input())
    num1=int((inNum/3)*2)
    num2=inNum-num1
    if num2+((num1//2)*2)==inNum:
        print(num2,num1//2)
    else:
        print(num1//2,num2)