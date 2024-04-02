#problem statement: https://codeforces.com/problemset/problem/141/A

str1 = input()
str2 = input()
jumble = sorted(list(input()))
nameStr=sorted(list(str1+str2))

if len(jumble)==len(nameStr):
    for i, j in zip(jumble,nameStr):
        if i!=j:
            print("NO")
            exit()
else:
    print("NO")
    exit()

print("YES")