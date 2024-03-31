#link to code: https://codeforces.com/problemset/problem/996/A

accBal=int(input())

denominations=[100,20,10,5,1]
denCnt=0
for i in denominations:
    if accBal==0:
        break
    if accBal%i!=accBal:
        denCnt+=(accBal//i)
        accBal%=i   


print(denCnt)