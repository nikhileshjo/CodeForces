soldierCnt=int(input())
soldierLineUp=list(map(int,input().split()))

maxHeightIndex=soldierLineUp.index(max(soldierLineUp))
minHeightIndex=soldierLineUp[::-1].index(min(soldierLineUp))


if (soldierCnt-minHeightIndex-1)<maxHeightIndex:
    timeReq=maxHeightIndex+minHeightIndex-1
else:
    timeReq=maxHeightIndex+minHeightIndex
print(timeReq)