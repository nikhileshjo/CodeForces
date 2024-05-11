#problem statement: https://codeforces.com/problemset/problem/1926/A

for _ in range(int(input())):
    inStr=input()
    Acnt=inStr.count('A')
    Bcnt=inStr.count('B')
    if Acnt>Bcnt:
        print('A')
    else:
        print('B')