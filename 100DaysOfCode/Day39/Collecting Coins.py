#problem statement: https://codeforces.com/problemset/problem/1294/A

testCnt=int(input())

for _ in range(testCnt):
    coinList=list(map(int,input().split()))
    n=coinList.pop()
    maxCoins=max(coinList)
    coinReq=(maxCoins-coinList[0])+(maxCoins-coinList[1])+(maxCoins-coinList[2])
    if coinReq<=n:
        if (n-coinReq)%3==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")