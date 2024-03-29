#Link to question: https://codeforces.com/problemset/problem/520/A

charCnt=int(input())
word=input().lower()
if charCnt<26:
    print("NO")
    exit()
else:
    for i in range(97,123):
        if chr(i) not in word:
            print("NO")
            exit()
        else:
            pass
print("YES")