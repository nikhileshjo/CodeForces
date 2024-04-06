#problem statement: https://codeforces.com/problemset/problem/581/A

sockCnt=list(map(int,input().split()))
fasCnt=min(sockCnt)
notFasCnt=(max(sockCnt)-min(sockCnt))//2
print(fasCnt,notFasCnt)