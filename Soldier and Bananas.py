cstFirst, moneyPocket, bananaCnt = (map(int,input().split()))
bCntSum = (bananaCnt*(1+bananaCnt))/2
totalCost=bCntSum*cstFirst
borrowed=int(totalCost-moneyPocket)
if borrowed<=0:
    print(0)
else:
    print(borrowed)
