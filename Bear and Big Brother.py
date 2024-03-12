lil, big = (map(int,input().split()))
cnt=0
while lil<=big:
    lil=lil*3
    big=big*2
    cnt+=1

print(cnt)