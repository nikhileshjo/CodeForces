stopCnt = int(input())
passengers=list()
minCapacity=0
currPass=0
for _ in range(stopCnt):
    passengers.append(list(map(int,input().split())))
for i in passengers:
    currPass=(currPass-i[0])+i[1]
    if minCapacity<currPass:
        minCapacity=currPass
print(minCapacity)