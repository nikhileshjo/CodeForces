qNum,cnt = (map(int,input().split()))
for _ in range(cnt):
    if qNum%10==0:
        qNum=qNum/10
    else:
        qNum-=1

print(int(qNum))