#problem statement: https://codeforces.com/problemset/problem/432/A

teamCnt,matchCnt=map(int,input().split())
partCnt=list(map(int,input().split()))
partCnt.sort()
result=0
if teamCnt>=3:
    qualStg=partCnt[2::3]    
    for i in qualStg:
        if i+matchCnt<=5:
            result+=1

print(result)