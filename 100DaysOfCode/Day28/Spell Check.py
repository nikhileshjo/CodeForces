#problem statement: https://codeforces.com/problemset/problem/1722/A

testCnt=int(input())
name="Timur"
for _ in range(testCnt):
    flag=True
    strLen=int(input())
    spelling=input()
    if strLen!=5:
        print("NO")
    else:
        for i in name:
            if i not in spelling:
                print("NO")
                flag=False
                break
        if flag:
            print("YES")
