#problem statement: https://codeforces.com/problemset/problem/1760/B

alphaList="abcdefghijklmnopqrstuvwxyz"

for _ in range(int(input())):
    strLn=input()
    maxAlpha=sorted(list(input()))[-1]
    print(alphaList.index(maxAlpha)+1)