#problem statement: https://codeforces.com/problemset/problem/703/A

rounds=int(input())

mWins=0
cWins=0
for _ in range(rounds):
    mDice,cDice=map(int,input().split())
    if mDice>cDice:
        mWins+=1
    elif cDice>mDice:
        cWins+=1
if mWins>cWins:
    print("Mishka")
elif cWins>mWins:
    print("Chris")
else:
    print("Friendship is magic!^^")