studCnt,tPassed = (map(int,input().split()))
queue = list(input())
flag=False
for _ in range(tPassed):
    flag=0
    for s in range(studCnt-1):
        if flag:
            flag=False
            continue
        if queue[s]<queue[s+1]:
            queue[s+1]='B'
            queue[s]='G'
            flag=True

result=''.join(queue)
print(result)