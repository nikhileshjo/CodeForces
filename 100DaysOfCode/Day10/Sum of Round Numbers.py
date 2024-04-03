#problem statement: https://codeforces.com/problemset/problem/1352/A

testCaseCnt=int(input())
result=[]
for _ in range(testCaseCnt):
    inNumb=input()[::-1]
    output=''
    outCnt=0
    for i in range(len(inNumb)):
        if int(inNumb[i]):
            output+=str(int(inNumb[i])*(10**i))+" "
            outCnt+=1
    result.append(outCnt)
    result.append(output)
for j in result:
    print(j)