#problem statement: https://codeforces.com/problemset/problem/381/A

cardCnt=int(input())
cards=list(map(int,input().split()))

Sereja=0
Dima=0

for i in range(1,cardCnt+1):
    if i%2==0:
        if cards[0]>cards[-1]:
            Dima+=cards[0]
            cards.pop(0)
        else:
            Dima+=cards[-1]
            cards.pop()
    else:
        if cards[0]>cards[-1]:
            Sereja+=cards[0]
            cards.pop(0)
        else:
            Sereja+=cards[-1]
            cards.pop()
print(Sereja,Dima)